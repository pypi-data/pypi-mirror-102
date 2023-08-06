import numpy as np
import matplotlib.pyplot as plt
import math
import os


class Vis_loss(object):
    def __init__(self, path):
        self.self_loss_dict = self._read_log(path)

    def _read_log(self, path):
        assert os.path.isfile(path)
        ret = {}
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith('(epoch'):
                    its = line.split(')')[-1].strip().split(' ')
                    for i in range(0, len(its), 2):
                        if its[i] not in ret.keys():
                            ret[its[i]] = [float(its[i + 1])]
                        else:
                            ret[its[i]] += [float(its[i + 1])]
        return ret

    def vis_log(self, loss_dict=None):
        if loss_dict is None:
            loss_dict = self.self_loss_dict
        fig_n = len(loss_dict.keys())
        hw = math.ceil(math.sqrt(fig_n))
        for i, cell in enumerate(loss_dict.items()):
            key, value = cell
            i += 1
            plt.subplot(hw * 100 + hw * 10 + i)
            plt.plot(np.array(range(len((value)))), value, color='red')
            plt.title(key)
        plt.show()


if __name__ == '__main__':
    d = {
        'fig1': np.sin(np.linspace(0, 2 * np.pi, 500)),
        'fig2': np.cos(np.linspace(0, 2 * np.pi, 500)),
        'fig3': np.cos(np.linspace(0, np.pi, 500))
    }
    vis_loss = Vis_loss('loss_log.txt')
    # vis_loss.vis_log(d)
    vis_loss.vis_log()