import logging
import matplotlib.pyplot as plt
import numpy as np


class Benchmark:

    def __init__(self, scanners):
        self.scanners = scanners
        self._grid_scan()

    @property
    def annealing_times(self):
        return [s.response['annealing_time'] for s in self.scanners]

    @property
    def chain_strengths(self):
        return [s.response['chain_strength'] for s in self.scanners]

    @property
    def errors(self):
        return [s.response['error'] for s in self.scanners]

    @property
    def num_scans(self):
        return len(self.scanners)

    @property
    def success_probabilities(self):
        return [s.response['success_probability'] for s in self.scanners]

    @property
    def two_sided_errors(self):
        lower = [min(s.response['success_probability'], s.response['error']) for s in self.scanners]
        upper = self.errors
        return [lower, upper]

    def _grid_scan(self):
        for i in range(self.num_scans):
            scanner = self.scanners[i]
            logging.info(f'Scan {i}/{self.num_scans}')

            if i > 0 and self.scanners[i - 1].response['success_probability'] == 0:
                logging.info(f'p = 0 for scan #{i}')
                self.scanners[i] = self.scanners[i - 1]
                continue

            scanner.grid_scan()


class Figure:

    def __init__(self):
        # Data
        self.x = []
        self.ys = []
        self.yerrs = []

        # Technical
        self.fig = plt.figure()
        self.ax = self.fig.subplots()

        # Display
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')

        self.kwargs = {
            'capsize': 2,
            'elinewidth': 1,
            'linewidth': 0,
            'marker': '.',
            'clip_on': False
        }

    def plot(self):
        for emb in range(len(self.ys)):
            self.ax.errorbar(self.x, self.ys[emb], yerr=self.yerrs[emb], **self.kwargs)


class ScanPlot(Figure):

    def __init__(self, scanner):
        super().__init__()

        self.scanner = scanner

        self._init_plot_data()
        self.plot()

    @property
    def ymin(self):
        y = np.array(self.ys)
        yerr = np.array(self.yerrs)
        return max(np.min(y + yerr), 0.)

    @property
    def ymax(self):
        y = np.array(self.ys)
        yerr = np.array(self.yerrs)
        return min(np.max(y + yerr), 1.)

    def plot(self):
        self.ax.set_ylabel('Success probability')

        if self.scanner.num_chain_strengths > 1:
            self.x = self.scanner.chain_strengths
            self.ax.set_xlabel('Relative chain strength')

        elif self.scanner.num_annealing_times > 1:
            self.x = self.scanner.annealing_times
            self.ax.set_xlabel('Annealing time $T$ in $\\mu\\mathrm{s}$')

        super().plot()

        xmin = self.x[0]
        xmax = self.x[-1]

        dx = (xmax - xmin) / 100.
        dy = (self.ymax - self.ymin) / 100.

        self.ax.set_xlim(xmin - dx, xmax + dx)
        self.ax.set_ylim(0, self.ymax + dy)

    def _init_plot_data(self):
        scanner = self.scanner

        for emb in range(scanner.num_embeddings):
            self.ys.append([])
            self.yerrs.append([])

            for cs in scanner.chain_strengths:
                for at in scanner.annealing_times:
                    n = scanner.num_samples
                    n_opt = scanner.results[emb, cs, at]
                    p = n_opt / n

                    self.ys[emb].append(p)
                    self.yerrs[emb].append(np.sqrt(p * (1 - p) / n))
