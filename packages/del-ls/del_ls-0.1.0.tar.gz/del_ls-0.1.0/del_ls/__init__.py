import math
import numpy


class SparseSquareMatrix:
    def __init__(self, row2idx, idx2col):
        ncols = row2idx.shape[0] - 1
        self.row2idx = row2idx
        self.idx2col = idx2col
        self.idx2val = numpy.zeros_like(idx2col, dtype=numpy.float64)
        self.row2val = numpy.zeros((ncols), dtype=numpy.float64)

    def set_zero(self):
        self.idx2val.fill(0.)
        self.row2val.fill(0.)

    # {y_vec} < - \alpha * [this_mat] * {x_vec} + \beta * {y_vec}
    def gemv(self, alpha, x_vec, beta, y_vec):
        from .del_ls import gemv
        gemv(self.row2idx, self.idx2col,
             self.row2val, self.idx2val,
             alpha, x_vec, beta, y_vec)

    def solve_cg(self, r_vec, max_iteration=1000, conv_ratio_tol=1.0e-5):
        u_vec = numpy.zeros_like(r_vec)
        p_vec = r_vec.copy()
        Ap_vec = numpy.zeros_like(r_vec)
        conv_hist = []
        sqnorm_res = r_vec.dot(r_vec)
        inv_sqnorm_res_ini = 1. / sqnorm_res
        for _iter in range(max_iteration):
            self.gemv(1., p_vec, 0., Ap_vec)
            pap = Ap_vec.dot(p_vec)
            alpha = sqnorm_res / pap
            u_vec += alpha * p_vec
            r_vec -= alpha * Ap_vec
            sqnorm_res_new = r_vec.dot(r_vec)
            conv_ratio = math.sqrt(sqnorm_res_new * inv_sqnorm_res_ini)
            conv_hist.append(conv_ratio)
            if conv_ratio < conv_ratio_tol:
                return u_vec, conv_hist
            beta = sqnorm_res_new / sqnorm_res
            sqnorm_res = sqnorm_res_new
            p_vec = r_vec + beta * p_vec
        return u_vec, conv_hist
