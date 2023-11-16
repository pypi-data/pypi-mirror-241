# -*- coding: latin-1 -*-
import skimage.transform

from morphonet.plugins import MorphoPlugin
import numpy as np
from ...tools import printv


class Stardist(MorphoPlugin):
    """ This plugin uses an intensity image of the nucleus from a local dataset at a specific time point, to compute a
    segmentation of the nucleus, using the 3D Stardist deep learning algorithm.

    Parameters
    ----------
    downsampling : int, default :2
        The resolution reduction applied to each axis of the input image before performing segmentation, 1 meaning that
        no reduction is applied. Increasing the reduction factor may reduce segmentation quality


    Reference : Uwe Schmidt, Martin Weigert, Coleman Broaddus, and Gene Myers. Cell Detection with Star-convex Polygons.
    International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI), Granada, Spain,
    September 2018.

    https://github.com/stardist/stardist

    """

    def __init__(self):  # PLUGIN DEFINITION
        MorphoPlugin.__init__(self)
        self.set_icon_name("Stardist.png")
        self.set_image_name("Stardist.png")
        self.set_name("Startdist : Perform nuclei segmentation on intensity images ")
        self.add_inputfield("downsampling", default=2)
        self.set_parent("Create Segmentation")
        self.set_description( "This plugin uses an intensity image of the nucleus from a local dataset at a specific time "
                              "point, to compute a segmentation of the nucleus, using the 3D Stardist deep learning algorithm.\n \n"
                             "Parameters : \n \n "
                             "- downsampling (numeric,default:2) : he resolution reduction applied to each axis of the "
                              "input image before performing segmentation, 1 meaning that no reduction is applied. "
                              "Increasing the reduction factor may reduce segmentation quality \n")


    def process(self, t, dataset, objects):  # PLUGIN EXECUTION
        if not self.start(t, dataset, objects, objects_require=False):
            return None

        from csbdeep.utils import normalize
        from stardist.models import StarDist3D
        from skimage.transform import resize

        Downsampled = int(self.get_inputfield("downsampling"))

        rawdata = dataset.get_raw(t)
        #rawdata = np.swapaxes(rawdata,0,2)
        cancel=False
        if rawdata is None:
            printv("please specify the rawdata",0)
            cancel=True
        else:
            data = np.zeros(rawdata.shape).astype(np.uint16)
            init_shape = rawdata.shape
            if Downsampled>1:
                rawdata=rawdata[::Downsampled,::Downsampled,::Downsampled]

            printv("normalize the rawdata",0)
            rawdata = normalize(rawdata)
            printv("load the stardist 3D model",0)
            model = StarDist3D.from_pretrained('3D_demo')

            printv("predict the nuclei",0)
            data, _ = model.predict_instances(rawdata)

            if Downsampled > 1:
                data = resize(data,init_shape,preserve_range=True,order=0)
            dataset.set_seg(t, data)
        self.restart(cancel=cancel)
