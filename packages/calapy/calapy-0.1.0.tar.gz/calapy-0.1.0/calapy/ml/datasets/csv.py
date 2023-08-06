# websites:
# https://pytorch.org/docs/stable/torchvision/transforms.html
# https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#sphx-glr-beginner-blitz-cifar10-tutorial-py
# https://pytorch.org/hub/pytorch_vision_resnet/
# https://discuss.pytorch.org/t/normalize-each-input-image-in-a-batch-independently-and-inverse-normalize-the-output/23739
# https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html

from .. import torch
import numpy as np
import math
import os
from .tools import Shifts
from ... import array as cp_array
from ... import txt as cp_txt
from ... import directory as cp_directory
from ... import maths as cp_maths
from ... import combinations as cp_combinations

__all__ = ['CSVLoader']


class CSVLoader:
    """
    A class used to load batches of samples

    Extended description

    Attributes
    ----------
    directory_root : str
        A formatted string to print out what the animal says
    shifts : Shifts
        The name of the animal
    L, n_levels_directories : int
        The number of the directory tree in the dataset.
    conditions_directories : sequence of sequences of ints
        The l_th element of the sequence contains the conditions of the l_th directory level that will be loaded

    Methods
    -------
    load_batches_e(order_outputs=None)
        It is a batch generator. It load a batch of samples at the time.
    """

    # TODO at the moment assumes that all dimensions of each file are within-sample or intra-sample.
    #  Add optional feature that allows loading the files that has one or more dimensions between-samples or
    #  inter-sample. In other words add file_axes_inter and file_axes_intra

    def __init__(
            self, directory_root,
            conditions_directories=None, levels_labels=None,
            levels_inter=None, levels_intra=None, rows=None, columns=None,
            inputs_axes_of_file_data=None, inputs_axis_of_samples=None,
            batch_size=None, n_batches=None, shuffle=False, shifts=None,
            device=None, order_outputs='il'):
        """
        Parameters
        ----------
        directory_root : str
            The directory of the dataset
        levels_labels : int or sequence of ints, optional
            The directory levels of the classes in the directory tree of the dataset.
        conditions_directories : None or sequence of Nones and sequences of ints, optional
            Conditions_directories can be a sequence or None (default is None). If it is a sequence, the l_th element
            of it is None or a sequence of ints. If the l_th element is a sequence of ints, it contains the conditions
            of the tree l_th level that will be loaded. If the l_th element is None all conditions of the l_th level
            will be loaded. If conditions_directories is None all conditions in all level will be loaded. It requires
            to be a sequence if n_levels_directories is None.
        order_outputs : str or sequence of str, optional
            The desired outputs of the self.load_batches_e(). Accepted values are "i", "l", "c","r", "a" or any
            combination of them like "ilcr", "ilr" (default is "il"). "i" stands for input samples, "l" for labels of
            the samples, "c" for combinations of the level conditions of the samples, "r" for the relative directories
            of the samples, "a" for the absolute directories of the samples.
        """

        self.directory_root = directory_root

        if levels_labels is None:
            self.levels_labels = np.asarray([], dtype='i')
        else:
            try:
                len(levels_labels)
                if isinstance(levels_labels, np.ndarray):
                    self.levels_labels = levels_labels
                else:
                    self.levels_labels = np.asarray(levels_labels, dtype='i')

                n_axes_levels_labels = len(self.levels_labels.shape)
                if n_axes_levels_labels > 1:
                    raise ValueError('levels_labels')

                self.n_labels = self.levels_labels.size
            except TypeError:
                self.levels_labels = np.asarray([levels_labels], dtype='i')
                self.n_labels = 1

        if levels_intra is None:
            self.levels_intra = np.asarray([], dtype='i')
        else:
            try:
                len(levels_intra)
                if isinstance(levels_intra, np.ndarray):
                    self.levels_intra = levels_intra
                else:
                    self.levels_intra = np.asarray(levels_intra, dtype='i')
            except TypeError:
                self.levels_intra = np.asarray([levels_intra], dtype='i')

        l = 0
        self.conditions_directories_names = []
        directory_root_l = self.directory_root
        while os.path.isdir(directory_root_l):
            self.conditions_directories_names.append(os.listdir(directory_root_l))
            directory_root_l = os.path.join(directory_root_l, self.conditions_directories_names[l][0])
            l += 1
        self.L = self.n_levels_directories = l
        del l, directory_root_l

        self.levels_intra[self.levels_intra < 0] += self.L
        self.levels_intra_sort = np.sort(self.levels_intra, axis=0)

        self.levels_all = np.arange(self.L, dtype='i')
        if any(cp_array.samples_in_arr1_are_not_in_arr2(self.levels_intra, self.levels_all)):
            raise ValueError('levels_intra')

        if levels_inter is None:
            self.levels_inter = (
                self.levels_all[cp_array.samples_in_arr1_are_not_in_arr2(self.levels_all, self.levels_intra)])
            self.levels_inter_sort = self.levels_inter
        else:
            try:
                len(levels_inter)
                if isinstance(levels_inter, np.ndarray):
                    self.levels_inter = levels_inter
                else:
                    self.levels_inter = np.asarray(levels_inter, dtype='i')
            except TypeError:
                self.levels_inter = np.asarray([levels_inter], dtype='i')

            self.levels_inter[self.levels_inter < 0] += self.L
            self.levels_inter_sort = np.sort(self.levels_inter, axis=0)

            if any(cp_array.samples_in_arr1_are_not_in_arr2(self.levels_inter, self.levels_all)):
                raise ValueError('levels_inter')

            if any(cp_array.samples_in_arr1_are_not_in_arr2(
                    self.levels_all, np.append(self.levels_inter, self.levels_intra, axis=0))):
                raise ValueError('self.levels_intra, levels_inter')

            if any(cp_array.samples_in_arr1_are_in_arr2(self.levels_inter, self.levels_intra)):
                raise ValueError('self.levels_intra, levels_inter')

        self.G = self.n_levels_directories_inter = self.levels_inter.size
        self.H = self.n_levels_directories_intra = self.levels_intra.size

        if conditions_directories is None:
            self.conditions_directories = [None] * self.L  # type: list
        else:
            try:
                conditions_directories[0]
            except TypeError:
                raise TypeError('conditions_directories')
            if len(conditions_directories) == self.L:
                self.conditions_directories = conditions_directories
            else:
                raise ValueError('conditions_directories')

        self.n_conditions_directories = np.empty(self.L, dtype='i')

        for l in range(self.L):
            if self.conditions_directories[l] is None:
                self.n_conditions_directories[l] = len(self.conditions_directories_names[l])
                self.conditions_directories[l] = np.arange(self.n_conditions_directories[l])
            else:
                self.n_conditions_directories[l] = len(self.conditions_directories[l])

        self.conditions_directories_names_inter = [None] * self.G  # type: list
        self.n_conditions_directories_inter = np.empty(self.G, dtype='i')
        self.conditions_directories_inter = [None] * self.G  # type: list
        g = 0
        for l in self.levels_inter:
            self.conditions_directories_names_inter[g] = self.conditions_directories_names[l]
            self.n_conditions_directories_inter[g] = self.n_conditions_directories[l]
            self.conditions_directories_inter[g] = self.conditions_directories[l]
            g += 1

        self.conditions_directories_names_intra = [None] * self.H  # type: list
        self.n_conditions_directories_intra = np.empty(self.H, dtype='i')
        self.conditions_directories_intra = [None] * self.H  # type: list
        h = 0
        for l in self.levels_intra:
            self.conditions_directories_names_intra[h] = self.conditions_directories_names[l]
            self.n_conditions_directories_intra[h] = self.n_conditions_directories[l]
            self.conditions_directories_intra[h] = self.conditions_directories[l]
            h += 1

        self.K = self.n_classes = self.n_conditions_directories[self.levels_labels]
        self.n_samples = cp_maths.prod(self.n_conditions_directories_inter)
        # self.n_samples = math.prod(self.n_conditions_directories)

        self.rows = rows
        self.columns = columns

        if batch_size is None:
            if n_batches is None:
                self.batch_size = self.n_samples
                self.n_batches = 1
            else:
                self.n_batches = n_batches
                self.batch_size = math.floor(self.n_samples / self.n_batches)
        else:
            self.batch_size = batch_size
            self.n_batches = math.floor(self.n_samples / self.batch_size)

        self.n_samples_e = self.n_batches * self.batch_size
        if self.n_samples_e < self.n_samples:
            print('Warming: self.n_samples_e < self.n_samples')

        self.shuffle = shuffle

        self.size_bin_indexes_samples = self.n_samples - self.n_samples_e

        self.indexes_samples = np.arange(self.n_samples)

        indexes_samples_e, self.bin_indexes_samples = (
            np.split(self.indexes_samples, [self.n_samples_e], axis=0))
        if not self.shuffle:
            self.batches_indexes = np.split(indexes_samples_e, self.n_batches, axis=0)

        self.shifts = shifts  # type: Shifts

        self.device = device

        self.order_accepted_values = 'ilcra'
        if order_outputs is None:
            self.order_outputs = 'il'
            self.n_outputs = 2
        else:
            self.order_outputs = order_outputs
            self.n_outputs = len(self.order_outputs)
            for o in range(self.n_outputs):
                if not (self.order_outputs[o] in self.order_accepted_values):
                    raise ValueError('order_outputs')

        self.outputs = [None] * self.n_outputs  # type: list

        self.return_inputs_eb = 'i' in self.order_outputs
        self.return_labels_eb = 'l' in self.order_outputs
        self.return_combinations_eb = 'c' in self.order_outputs
        self.return_relative_directories_eb = 'r' in self.order_outputs
        self.return_absolute_directories_eb = 'a' in self.order_outputs

        print('self.batch_size =', self.batch_size)
        print('self.n_batches =', self.n_batches)
        print('self.n_samples_e =', self.n_samples_e)
        print('self.n_samples =', self.n_samples)
        print('self.shifts =', self.shifts)
        print('self.n_conditions_directories =', self.n_conditions_directories)
        # print('self.conditions_directories =', self.conditions_directories)

        self.levels_shifts_inter = []
        self.ranges_shifts_inter = []

        self.levels_shifts_intra = []
        self.ranges_shifts_intra = []

        if self.shifts is not None:
            self.shifts.levels[self.shifts.levels < 0] += self.L

            for v in range(self.shifts.n_levels):
                if self.shifts.levels[v] in self.levels_inter:
                    self.levels_shifts_inter.append(np.where(self.shifts.levels[v] == self.levels_inter)[0][0].tolist())
                    self.ranges_shifts_inter.append(self.shifts.ranges[v])
                elif self.shifts.levels[v] in self.levels_intra:
                    self.levels_shifts_intra.append(np.where(self.shifts.levels[v] == self.levels_intra)[0][0].tolist())
                    self.ranges_shifts_intra.append(self.shifts.ranges[v])

            if len(self.levels_shifts_inter) == 0:
                self.shifts_inter = None
            else:
                self.shifts_inter = Shifts(self.ranges_shifts_inter, self.levels_shifts_inter, self.n_samples)
                self.levels_shifts_inter = self.shifts_inter.levels
                self.levels_shifts_inter_sort = self.shifts_inter.levels_sort
                self.ranges_shifts_inter = self.shifts_inter.ranges

            if len(self.levels_shifts_intra) == 0:
                self.shifts_intra = None
            else:
                self.shifts_intra = Shifts(self.ranges_shifts_intra, self.levels_shifts_intra, self.batch_size)
                self.levels_shifts_intra = self.shifts_intra.levels
                self.levels_shifts_intra_sort = self.shifts_intra.levels_sort
                self.ranges_shifts_intra = self.shifts_intra.ranges
            # if self.shifts.n_shifts is None:
            #     self.shifts.set_n_shifts(self.n_samples)

        if self.shifts_inter is not None:
            self.combinations_directories_inter_no_shift = (
                cp_combinations.conditions_to_combinations(self.conditions_directories_inter))
            self.combinations_directories_inter = None
            self.labels = None

        else:
            self.combinations_directories_inter_no_shift = None
            self.combinations_directories_inter = (
                cp_combinations.conditions_to_combinations(self.conditions_directories_inter))
            if self.return_labels_eb:
                self.labels = torch.tensor(
                    self.combinations_directories_inter[slice(0, self.n_samples, 1), np.squeeze(self.levels_labels)],
                    dtype=torch.int64, device=self.device)
            else:
                self.labels = None

        if self.shifts_intra is not None:
            self.combinations_directories_intra_no_shift = (
                cp_combinations.conditions_to_combinations(self.conditions_directories_intra))
            self.combinations_directories_intra = None

        else:
            self.combinations_directories_intra_no_shift = None
            self.combinations_directories_intra = (
                cp_combinations.conditions_to_combinations(self.conditions_directories_intra))

        self.combinations_indexes_input_intra = (
            cp_combinations.n_conditions_to_combinations(self.n_conditions_directories_intra))

        combination_directory_str_0 = [self.conditions_directories_names[l][0] for l in range(self.L)]
        directory_0 = os.path.join(self.directory_root, *combination_directory_str_0)
        self.format_files = cp_directory.get_extension(directory_0, point=False).lower()

        array_np_0 = cp_txt.csv_file_to_array(directory_0, rows=self.rows, columns=self.columns, dtype='f')
        tensor_0 = torch.tensor(array_np_0, dtype=torch.float32, device=self.device)

        shape_file_0 = list(tensor_0.shape)
        self.shape_files = shape_file_0
        self.n_dims_files = self.shape_files.__len__()

        self.n_dims_samples = self.n_dims_files + self.H
        self.n_dims_batch = self.n_dims_samples + 1

        self.n_dims_directories_eb = self.H + 1

        if inputs_axes_of_file_data is None:
            self.inputs_axes_of_file_data = np.arange(
                self.n_dims_batch - self.n_dims_files, self.n_dims_batch, 1, dtype='i')
        else:
            try:
                len(inputs_axes_of_file_data)
                if isinstance(inputs_axes_of_file_data, np.ndarray):
                    self.inputs_axes_of_file_data = inputs_axes_of_file_data
                else:
                    self.inputs_axes_of_file_data = np.asarray(inputs_axes_of_file_data, dtype='i')
            except TypeError:
                self.inputs_axes_of_file_data = np.asarray([inputs_axes_of_file_data], dtype='i')

        self.inputs_axes_of_file_data[self.inputs_axes_of_file_data < 0] += self.n_dims_batch

        self.inputs_axes = np.arange(0, self.n_dims_batch, 1, dtype='i')

        if inputs_axis_of_samples is None:
            self.inputs_axis_of_samples = 0
            while self.inputs_axis_of_samples in self.inputs_axes_of_file_data:
                self.inputs_axis_of_samples += 1
        elif inputs_axis_of_samples in self.inputs_axes_of_file_data:
            if inputs_axes_of_file_data is None:
                if inputs_axis_of_samples < 0:
                    self.inputs_axis_of_samples = inputs_axis_of_samples + self.n_dims_batch
                else:
                    self.inputs_axis_of_samples = inputs_axis_of_samples
                self.inputs_axes_of_file_data[self.inputs_axes_of_file_data <= self.inputs_axis_of_samples] -= 1
            else:
                raise ValueError('inputs_axis_of_samples, inputs_axes_of_file_data')
        else:
            self.inputs_axis_of_samples = inputs_axis_of_samples

        if self.inputs_axis_of_samples < 0:
            self.inputs_axis_of_samples += self.n_dims_batch

        inputs_axes_of_non_intra = np.sort(np.append(self.inputs_axis_of_samples, self.inputs_axes_of_file_data))

        self.inputs_axes_of_intra = np.empty(self.H, dtype='i')

        if len(self.inputs_axes_of_intra) > 0:

            self.inputs_axes_of_intra[0] = 0

            while self.inputs_axes_of_intra[0] in inputs_axes_of_non_intra:
                self.inputs_axes_of_intra[0] += 1

        for h in range(1, self.H):
            self.inputs_axes_of_intra[h] = self.inputs_axes_of_intra[h - 1] + 1
            while self.inputs_axes_of_intra[h] in inputs_axes_of_non_intra:
                self.inputs_axes_of_intra[h] += 1

        self.input_axes_of_sample_data = self.inputs_axes[cp_array.samples_in_arr1_are_not_in_arr2(
            self.inputs_axes, self.inputs_axis_of_samples)]

        # self.batch_axes_of_intra = (
        #     self.batch_axes[cp_array.samples_in_arr1_are_not_in_arr2(self.batch_axes, self.inputs_axes_of_file_data)])

        self.shape_batch = np.empty(self.n_dims_batch, dtype='i')
        self.shape_batch[self.inputs_axis_of_samples] = self.batch_size
        self.shape_batch[self.inputs_axes_of_intra] = self.n_conditions_directories_intra
        self.shape_batch[self.inputs_axes_of_file_data] = self.shape_files

        # self.shape_samples = tuple(self.shape_batch[self.input_axes_of_sample_data].tolist())
        # self.shape_batch = tuple(self.shape_batch.tolist())
        # self.shape_files = tuple(self.shape_files)

        # self.shape_samples = tuple(np.append(self.n_conditions_directories_intra, self.shape_files, axis=0).tolist())
        # self.shape_batch = tuple(np.append([self.batch_size], self.shape_samples, axis=0).tolist())

        if self.return_inputs_eb:

            self.inputs_eb = torch.empty(tuple(self.shape_batch.tolist()), dtype=torch.float32, device=self.device)
        else:
            self.inputs_eb = None

        self.directory_axes_of_intra = []
        self.directory_axis_of_samples = None

        f = 0
        for i in self.inputs_axes:
            if i in self.inputs_axes_of_file_data:
                f += 1
            elif i in self.inputs_axes_of_intra:
                self.directory_axes_of_intra.append(i - f)
            elif i == self.inputs_axis_of_samples:
                self.directory_axis_of_samples = i - f

        self.indexes_batch = np.empty(self.n_dims_batch, dtype='O')
        for d in range(0, self.n_dims_batch, 1):
            self.indexes_batch[d] = slice(0, self.shape_batch[d], 1)

        self.directory_axes_of_intra = np.asarray(self.directory_axes_of_intra, dtype='i')

        self.shape_directories_eb = np.empty(self.n_dims_directories_eb, dtype='i')
        self.shape_directories_eb[self.directory_axes_of_intra] = self.shape_batch[self.inputs_axes_of_intra]
        self.shape_directories_eb[self.directory_axis_of_samples] = self.shape_batch[self.inputs_axis_of_samples]

        if self.return_relative_directories_eb:
            self.relative_directories_eb = np.empty(self.shape_directories_eb, dtype='O')

        else:
            self.relative_directories_eb = None

        if self.return_absolute_directories_eb:
            self.absolute_directories_eb = np.empty(self.shape_directories_eb, dtype='O')
        else:
            self.absolute_directories_eb = None

        self.n_dims_directories_eb = self.shape_directories_eb.size
        self.indexes_directories_ebij = np.empty(self.n_dims_directories_eb, dtype='O')

        self.combinations_ebij = np.empty(self.L, dtype='i')

        print('self.shape_batch =', self.shape_batch)
        print()

    def __iter__(self):
        return self

    def __next__(self):

        """
        short description

        long description

        Returns
        -------
        out : generator
            A generator of lists of elements requested in order_outputs. The elements have the same order as in
            order_outputs. It generates a list per batch of input samples.

        Raises
        ------
        ValueError
            something

        """

        if self.shifts_inter is not None:
            self.shifts_inter.next()
            # TODO: recopy only the variable conditions with shifts
            self.combinations_directories_inter = np.copy(self.combinations_directories_inter_no_shift)
            self.combinations_directories_inter[:, self.shifts_inter.levels] += self.shifts_inter.values
            if self.return_labels_eb:
                self.labels = torch.tensor(
                    self.combinations_directories_inter[slice(0, self.n_samples, 1), np.squeeze(self.levels_labels)],
                    dtype=torch.int64, device=self.device)
            else:
                self.labels = None

        if self.shifts_intra is not None:
            self.shifts_intra.next()

        if self.shuffle:
            indexes_samples_e = np.append(self.indexes_samples, self.bin_indexes_samples, axis=0)
            indexes_samples_e, self.bin_indexes_samples = (
                np.split(np.random.permutation(indexes_samples_e), [self.n_samples_e], axis=0))
            self.batches_indexes = np.split(indexes_samples_e, self.n_batches, axis=0)
            self.size_bin_indexes_samples = len(self.bin_indexes_samples)

        for b in range(self.n_batches):
            if self.return_labels_eb:
                labels_eb = self.labels[self.batches_indexes[b]]

            combinations_inter_eb = self.combinations_directories_inter[self.batches_indexes[b], :]
            # batch_size_eb = batches_indexes_e.shape[0]
            for i in range(self.batch_size):

                self.indexes_batch[self.inputs_axis_of_samples] = i
                self.indexes_directories_ebij[self.directory_axis_of_samples] = i

                if self.shifts_intra is not None:
                    # TODO: recopy only the variable conditions with shifts
                    self.combinations_directories_intra = np.copy(self.combinations_directories_intra_no_shift)
                    self.combinations_directories_intra[:, self.shifts_intra.levels] += (
                        self.shifts_intra.values[slice(i, i + 1, 1), :])

                combination_inter_ebi = combinations_inter_eb[i, :]

                self.combinations_ebij[self.levels_inter] = combination_inter_ebi

                if self.combinations_directories_intra.shape[0] > 0:


                    for j in range(self.combinations_directories_intra.shape[0]):

                        combination_intra_ebij = self.combinations_directories_intra[j, :]

                        self.combinations_ebij[self.levels_intra] = combination_intra_ebij

                        combination_directory_str_ebij = [
                            self.conditions_directories_names[l][self.combinations_ebij[l]] for l in range(self.L)]

                        relative_directory_ebij = os.path.join(*combination_directory_str_ebij)
                        absolute_directory_ebij = os.path.join(self.directory_root, relative_directory_ebij)

                        if self.return_inputs_eb:
                            self.indexes_batch[self.inputs_axes_of_intra] = self.combinations_indexes_input_intra[j, :]

                            array_np_ebij = cp_txt.csv_file_to_array(
                                absolute_directory_ebij, rows=self.rows, columns=self.columns, dtype='f')
                            tensor_ebij = torch.tensor(array_np_ebij, dtype=torch.float32, device=self.device)

                            # todo move dimensions of tensor_ebi
                            #  if inputs_axes_of_file_data[0] > inputs_axes_of_file_data[1]

                            self.inputs_eb[tuple(self.indexes_batch)] = tensor_ebij

                        self.indexes_directories_ebij[self.directory_axes_of_intra] = (
                            self.combinations_indexes_input_intra[j, :])

                        if self.return_relative_directories_eb:
                            self.relative_directories_eb[tuple(self.indexes_directories_ebij)] = relative_directory_ebij

                        if self.return_absolute_directories_eb:
                            self.absolute_directories_eb[tuple(self.indexes_directories_ebij)] = absolute_directory_ebij

                else:
                    combination_directory_str_ebij = [
                        self.conditions_directories_names[l][self.combinations_ebij[l]] for l in range(self.L)]

                    relative_directory_ebij = os.path.join(*combination_directory_str_ebij)
                    absolute_directory_ebij = os.path.join(self.directory_root, relative_directory_ebij)

                    if self.return_inputs_eb:

                        array_np_ebij = cp_txt.csv_file_to_array(
                            absolute_directory_ebij, rows=self.rows, columns=self.columns, dtype='f')

                        tensor_ebij = torch.tensor(array_np_ebij, dtype=torch.float32, device=self.device)
                        # todo move dimensions of tensor_ebi
                        #  if inputs_axes_of_file_data[0] > inputs_axes_of_file_data[1]

                        self.inputs_eb[tuple(self.indexes_batch)] = tensor_ebij

                    if self.return_relative_directories_eb:
                        self.relative_directories_eb[tuple(self.indexes_directories_ebij)] = relative_directory_ebij

                    if self.return_absolute_directories_eb:
                        self.absolute_directories_eb[tuple(self.indexes_directories_ebij)] = absolute_directory_ebij

            for o in range(self.n_outputs):
                if self.order_outputs[o] == 'i':
                    self.outputs[o] = self.inputs_eb
                elif self.order_outputs[o] == 'l':
                    self.outputs[o] = labels_eb
                elif self.order_outputs[o] == 'c':
                    self.outputs[o] = combinations_inter_eb
                elif self.order_outputs[o] == 'r':
                    self.outputs[o] = self.relative_directories_eb
                elif self.order_outputs[o] == 'a':
                    self.outputs[o] = self.absolute_directories_eb

            return self.outputs
