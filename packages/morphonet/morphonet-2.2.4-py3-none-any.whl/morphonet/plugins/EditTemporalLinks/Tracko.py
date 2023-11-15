# -*- coding: latin-1 -*-
from morphonet.plugins import MorphoPlugin
from morphonet.tools import printv


def get_iou(bb1, bb2):
    '''
    Calculate the Intersection over Union (IoU) of two bounding boxes.
    '''

    # determine the coordinates of the intersection rectangle
    x_left = max(bb1[0], bb2[0])
    y_top = max(bb1[1], bb2[1])
    z_up = max(bb1[2], bb2[2])
    x_right = min(bb1[3], bb2[3])
    y_bottom = min(bb1[4], bb2[4])
    z_down = min(bb1[5], bb2[5])

    if x_right < x_left or y_bottom < y_top  or z_down< z_up :
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = (x_right - x_left) * (y_bottom - y_top) * (z_down - z_up)

    # compute the area of both AABBs
    bb1_area = (bb1[3] - bb1[0]) * (bb1[4] - bb1[1]) * (bb1[5] - bb1[2])
    bb2_area = (bb2[3] - bb2[0]) * (bb2[4] - bb2[1]) * (bb2[5] - bb2[2])

    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    return iou



def get_best_oberlap(bbox,bboxs):
    o=0
    best=None
    #computing the best = one by one computing
    for mo in bboxs:
        #get the iou count for the box
        ov=get_iou(bbox,bboxs[mo])
        #if iou is more than the previous best, choose this box
        if ov>o:
            o=ov
            best=mo
    return best




class Tracko(MorphoPlugin):
    """This plugin creates a complete object lineage using the maximum of overlap between objects.
    The overlap is calculated between the bounding box enveloping each object. After the execution, the lineage property
    is updated, and sent back to MorphoNet.


    Parameters
    ----------
    time direction : dropdown
        Forward : The  tracking is performed from the the current time point to last one
        Backward : The tracking is performed from the the current time point to first one

    """
    def __init__(self): #PLUGIN DEFINITION
        MorphoPlugin.__init__(self)
        self.set_image_name("Tracko.png")
        self.set_icon_name("Tracko.png")
        self.set_name("Track : Create temporal links on all objects using maks overlap between time steps")
        self.set_parent("Edit Temporal Links")
        self.add_dropdown("time direction", ["forward", "backward"])
        self.add_dropdown("optical flow", ["none","TV-L1", "iLK"])
        self.set_description("This plugin creates a complete object lineage using the maximum of overlap between objects. "
                             "The overlap is calculated between the bounding box enveloping each object."
                             " After the execution, the lineage property is updated, and sent back to MorphoNet..\n \n"
                              "Parameters : \n \n "
                             "- time direction : Direction of tracking \n "
                             "    Forward : from the the current time point to last one \n"
                             "    Backward : from the the current time point to first one \n ")

    def process(self,t,dataset,objects): #PLUGIN EXECUTION
        if not self.start(t,dataset,objects,objects_require=False):
            return None
        #Get the lineage propagation direction
        direction=self.get_dropdown("time direction")
        optical=self.get_dropdown("optical flow")
        printv("start overlap tracking from "+str(t),0)
        if direction=="forward" :
            while t<self.dataset.end: #From t to t max
                self.compute_links(t,t+1) #compute lineage by overlaping
                t+=1
        if direction == "backward":
            while t > self.dataset.begin: #from t to t min
                self.compute_links(t, t - 1) # compute lineage by overlaping
                t -= 1

        self.restart()

    def compute_links(self,t, tp):
        printv("compute links at " + str(t), 0)

        bboxs = self.dataset.get_regionprop_at("bbox", t) #Get the different cells bounding box
        next_bboxs = self.dataset.get_regionprop_at("bbox", tp) #Get the next time points bounding box
        for mo in bboxs:
            next_mo = get_best_oberlap(bboxs[mo], next_bboxs) #For each box at t , find the best overlapping one at t+1
            self.dataset.add_daughter(mo, next_mo) #link the corresponding cells in lineage
