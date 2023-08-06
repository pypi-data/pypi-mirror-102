import math
import sys

import numpy as np
import matplotlib.pyplot as plt
from dtaidistance import dtw
from numpy.core.tests.test_mem_overlap import xrange
from scipy.stats import mode
from scipy.spatial.distance import squareform
from sklearn.preprocessing import normalize

plt.style.use('bmh')

try:
    from IPython.display import clear_output

    have_ipython = True
except ImportError:
    have_ipython = False


class LBEnhanced:

    @staticmethod
    def distance(A: [], B: [], U: [], L: [], W, v, cutoffvalue=None):
        dists = list()
        n = len(A)
        m = len(B)
        l = n - 1
        n_bands = min(l / 2, v)
        last_index = l - n_bands
        d_inicial = A[0] - B[0]
        d_final = A[l] - B[m - 1]
        res = d_inicial * d_inicial + d_final * d_final

        i = 1
        while i < n_bands:
            right_end = l - i
            minL = A[i] - B[i]
            minL = minL * minL
            minR = A[right_end] - B[right_end]
            minR = minR * minR
            j = int(max(0, i - W))
            while j < i:
                right_start = l - j
                tmp = A[j] - B[j]
                minL = min(minL, tmp * tmp)
                tmp = A[j] - B[j]
                minL = min(minL, tmp * tmp)
                tmp = A[right_end] - B[right_start]
                minR = min(minR, tmp * tmp)
                tmp = A[right_start] - B[right_end]
                minR = min(minR, tmp * tmp)
                j = j + 1
            relative_res = minL + minR
            dists.append(relative_res)
            res = res + minL + minR
            i = i + 1
        if cutoffvalue is not None and res >= cutoffvalue:
                return dtw.lb_keogh(A, B, window=W)
        i = int(n_bands)
        while i <= last_index:
            a_val = A[i]
            if a_val > U[i]:
                tmp = a_val - U[i]
                res = res + tmp * tmp
            elif a_val < L[i]:
                tmp = L[i] - a_val
                res = res + tmp * tmp
            i = i + 1
        return res

    @staticmethod
    def distance_without_keogh(A, B, W, n_bands, keogh_distance):
        array_A = A.get_array_serie()
        array_B = B.get_array_serie()
        n = len(array_A)
        m = len(array_B)
        l = n - 1
        d_inicial = array_A[0] - array_B[0]
        d_final = array_A[n - 1] - array_B[m - 1]
        res = d_inicial * d_inicial + d_final * d_final + keogh_distance

        for i in range(1, n_bands):
            right_end = l - i
            minL = array_A[i] - array_B[i]
            minL = minL * minL
            minR = array_A[right_end] - array_B[right_end]
            minR = minR * minR
            j = max(0, i - W)
            while j < i:
                right_start = l - j
                tmp = array_A[i] - array_B[j]
                minL = min(minL, tmp * tmp)
                tmp = array_A[j] - array_B[i]
                minL = min(minL, tmp * tmp)
                tmp = array_A[right_end] - array_B[right_start]
                minR = min(minR, tmp * tmp)
                tmp = array_A[right_start] - array_B[right_end]
                minR = min(minR, tmp * tmp)
                j = j + 1
            res = res + minL + minR
        return res



class SequenceStats:

    def __init__(self, dataset=None, window=0):
        self.n_seq = len(dataset)
        self.seq_len = len(dataset[0])

        self.upper_envelope = np.zeros([self.n_seq, self.seq_len])
        self.lower_envelope = np.zeros([self.n_seq, self.seq_len])
        self.upper_rear_envelope = np.zeros([self.n_seq, self.seq_len])
        self.lower_rear_envelope = np.zeros([self.n_seq, self.seq_len])
        self.upper_front_envelope = np.zeros([self.n_seq, self.seq_len])
        self.lower_front_envelope = np.zeros([self.n_seq, self.seq_len])

        self.sorted_sequence = np.zeros([self.n_seq, self.seq_len, self.seq_len])
        self.first_3sorted = np.zeros([self.n_seq, 3])
        self.last_3sorted = np.zeros([self.n_seq, 3])

        self.dataset = dataset
        self.mins = np.zeros([self.n_seq])
        self.maxs = np.zeros([self.n_seq])
        self.index_mins = np.zeros([self.n_seq])
        self.index_maxs = np.zeros([self.n_seq])
        self.is_min_first = np.zeros([self.n_seq])
        self.is_min_last = np.zeros([self.n_seq])
        self.is_max_first = np.zeros([self.n_seq])
        self.is_max_last = np.zeros([self.n_seq])
        self.indices_sorted = np.zeros([self.n_seq, self.seq_len, 2])

        for i in range(0, len(self.dataset)):
            minimum = sys.float_info.min
            maximum = sys.float_info.max
            index_min = -1
            index_max = -1
            for j in range(0, len(self.dataset[i])):
                elt = dataset[i][j]
                if elt > maximum:
                    maximum = elt
                    index_max = j
                if elt < minimum:
                    minimum = elt
                    index_min = j
                self.indices_sorted[i][j][0] = j
                self.indices_sorted[i][j][1] = abs(elt)
            self.index_maxs[i] = index_max
            self.index_mins[i] = index_min
            self.mins[i] = minimum
            self.maxs[i] = maximum
            self.is_min_first[i] = (index_min == 0)
            self.is_min_last[i] = (index_min == (len(self.dataset[i]) - 2))
            self.is_max_first[i] = (index_max == 0)
            self.is_max_last[i] = (index_max == (len(self.dataset[i]) - 2))
        self.indices_sorted = np.sort(self.indices_sorted)[::-1]
        self.set_all_envelopes(window)

    def set_dataset(self, dt):
        self.__init__(dt)

    def set_all_envelopes(self, window):
        for index in range(0, self.n_seq):
            sequence = self.dataset[index]
            length = len(sequence)
            for i in range(0, length):
                minimo = math.inf
                maximo = -math.inf
                min_rear = math.inf
                max_rear = -math.inf
                min_front = math.inf
                max_front = -math.inf
                start_w = max(0, i - window)
                stop_w = min(length - 1, i + window)
                j = start_w
                while j <= stop_w:
                    value = sequence[j]
                    minimo = min(minimo, value)
                    maximo = max(maximo, value)
                    if j <= i:
                        min_rear = min(min_rear, value)
                        max_rear = max(max_rear, value)
                    if j >= i:
                        min_front = min(min_front, value)
                        max_front = max(max_front, value)
                    j = j + 1
                self.lower_envelope[index][i] = minimo
                self.upper_envelope[index][i] = maximo
                self.lower_rear_envelope[index][i] = min_rear
                self.upper_rear_envelope[index][i] = max_rear
                self.lower_front_envelope[index][i] = min_front
                self.upper_front_envelope[index][i] = max_front

    def init_keogh(self, dataset):
        self.n_seq = dataset.num_instances()
        self.seq_len = dataset.get_instance(0).num_series()
        self.upper_envelope = np.array([self.n_seq, self.seq_len])
        self.lower_envelope = np.array([self.n_seq, self.seq_len])
        self.dataset = dataset


class KnnLb(object):
    """K-nearest neighbor classifier using dynamic time warping
    as the distance measure between pairs of time series arrays

    Arguments
    ---------
    n_neighbors : int, optional (default = 5)
        Number of neighbors to use by default for KNN

    max_warping_window : int, optional (default = infinity)
        Maximum warping window allowed by the DTW dynamic
        programming function

    subsample_step : int, optional (default = 1)
        Step size for the timeseries array. By setting subsample_step = 2,
        the timeseries length will be reduced by 50% because every second
        item is skipped. Implemented by x[:, ::subsample_step]
    """

    def __init__(self, n_neighbors=5, max_warping_window=10000, subsample_step=1, window=5, V=20):
        self.n_neighbors = n_neighbors
        self.max_warping_window = max_warping_window
        self.subsample_step = subsample_step
        self.window = window
        self.V = V

    def fit(self, x, y, train_cache, test_cache):
        """Fit the model using x as training data and l as class labels

        Arguments
        ---------
        x : array of shape [n_samples, n_timepoints]
            Training data set for input into KNN classifer

        l : array of shape [n_samples]
            Training labels for input into KNN classifier
        """
        self.x = x
        self.y = y
        self.train_cache = train_cache
        self.test_cache = test_cache

    def _dist_matrix_lb(self, x, y):
        """Computes the M x N distance matrix between the training
        dataset and testing dataset (y) using the LB_Enhanced distance measure

        Arguments
        ---------
        x : array of shape [n_samples, n_timepoints]

        y : array of shape [n_samples, n_timepoints]

        Returns
        -------
        Distance matrix between each item of x and y with
            shape [training_n_samples, testing_n_samples]
        """

        # Compute the distance matrix
        dm_count = 0

        # Compute condensed distance matrix (upper triangle) of pairwise dtw distances
        # when x and y are the same array
        if np.array_equal(x, y):
            x_s = np.shape(x)
            dm = np.zeros((x_s[0] * (x_s[0] - 1)) // 2, dtype=np.double)
            best_distance = np.inf
            for i in xrange(0, x_s[0] - 1):
                for j in xrange(i + 1, x_s[0]):
                    U = self.train_cache.upper_envelope[i]
                    L = self.train_cache.lower_envelope[i]
                    w = self.window
                    v = self.V
                    dm[dm_count] = self.lb_enhanced_distance(x[i, ::self.subsample_step],
                                                             y[j, ::self.subsample_step], U, L, w, v, best_distance)
                    if best_distance > dm[dm_count]:
                        best_distance = dm[dm_count]
                    dm_count += 1
            # Convert to squareform
            dm = squareform(dm)
            return dm
        # Compute full distance matrix of dtw distnces between x and y
        else:
            x_s = np.shape(x)
            y_s = np.shape(y)
            dm = np.zeros((x_s[0], y_s[0]))
            for i in xrange(0, x_s[0]):
                for j in xrange(0, y_s[0]):
                    U = self.train_cache.upper_envelope[i]
                    L = self.train_cache.lower_envelope[i]
                    dm[i, j] = self.lb_enhanced_distance(x[i, ::self.subsample_step],
                                                         y[j, ::self.subsample_step], U, L, self.window, self.V)
                    # Update progress bar
                    dm_count += 1
            return dm

    def _dist_simple_matrix_lb(self, x, y, train_cache, window, V):
        dm_count = 0
        x_s = np.shape(x)
        y_s = np.shape(y)
        dm = np.zeros((1, y_s[0]))
        dm_size = x_s[0] * y_s[0]

        for j in xrange(0, y_s[0]):
            U = train_cache.upper_envelope[0]
            L = train_cache.lower_envelope[0]
            dm[0, j] = self.lb_enhanced_distance(x, y[j, ::self.subsample_step], U, L, window, V)
        return dm

    def predict(self, x):

        dm = self._dist_simple_matrix_lb(x, self.x, self.train_cache, self.window, self.V)

        # Identify the k nearest neighbors
        knn_idx = dm.argsort()[:, :self.n_neighbors]

        # Identify k nearest labels
        knn_labels = self.y[knn_idx]

        # Model Label
        mode_data = mode(knn_labels, axis=0)
        mode_label = mode_data[0]
        return mode_label.ravel()[0]

    def predict_proba(self, x, train_cache, window, V):
        """Predict the class labels or probability estimates for
        the provided data

        Arguments
        ---------
          x : array of shape [n_samples, n_timepoints]
              Array containing the testing data set to be classified

        Returns
        -------
          2 arrays representing:
              (1) the predicted class labels
              (2) the knn label count probability
        """

        dm = self._dist_matrix_lb(x, self.x)

        # Identify the k nearest neighbors
        knn_idx = dm.argsort()[:, :self.n_neighbors]

        # Identify k nearest labels
        knn_labels = self.y[knn_idx]

        # Model Label
        mode_data = mode(knn_labels, axis=1)
        mode_label = mode_data[0]
        mode_proba = mode_data[1] / self.n_neighbors

        return mode_label.ravel(), mode_proba.ravel()

    @staticmethod
    def lb_enhanced_distance(A: [], B: [], U: [], L: [], W, v, cutoffvalue=None):
        dists = list()
        n = len(A)
        m = len(B)
        l = n - 1
        n_bands = min(l / 2, v)
        last_index = l - n_bands
        d_inicial = A[0] - B[0]
        d_final = A[l] - B[m - 1]
        res = d_inicial * d_inicial + d_final * d_final
        i = 1
        while i < n_bands:
            right_end = l - i
            minL = A[i] - B[i]
            minL = minL * minL
            minR = A[right_end] - B[right_end]
            minR = minR * minR
            j = int(max(0, i - W))
            while j < i:
                right_start = l - j
                tmp = A[j] - B[j]
                minL = min(minL, tmp * tmp)
                tmp = A[j] - B[j]
                minL = min(minL, tmp * tmp)
                tmp = A[right_end] - B[right_start]
                minR = min(minR, tmp * tmp)
                tmp = A[right_start] - B[right_end]
                minR = min(minR, tmp * tmp)
                j = j + 1
            relative_res = minL + minR
            dists.append(relative_res)
            res = res + minL + minR
            i = i + 1
        if cutoffvalue is not None and res >= cutoffvalue:
            return dtw.lb_keogh(A, B, window=W)
        i = int(n_bands)
        while i <= last_index:
            a_val = A[i]
            if a_val > U[i]:
                tmp = a_val - U[i]
                res = res + tmp * tmp
            elif a_val < L[i]:
                tmp = L[i] - a_val
                res = res + tmp * tmp
            i = i + 1
        return res
