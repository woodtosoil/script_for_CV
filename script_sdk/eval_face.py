# Copyright (c) 2017-present, Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################
#
# Based on:
# --------------------------------------------------------
# Fast/er R-CNN
# Licensed under The MIT License [see LICENSE for details]
# Written by Bharath Hariharan
# --------------------------------------------------------

"""Python implementation of the PASCAL VOC devkit's AP evaluation code."""

import pickle
import logging
import numpy as np
import os
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)


def parse_rec(filename):
    """Parse a PASCAL VOC xml file."""
    tree = ET.parse(filename)
    objects = []
    for obj in tree.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        obj_struct['pose'] = obj.find('pose').text
        obj_struct['truncated'] = int(obj.find('truncated').text)
        obj_struct['difficult'] = int(obj.find('difficult').text)
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(bbox.find('xmin').text),
                              int(bbox.find('ymin').text),
                              int(bbox.find('xmax').text),
                              int(bbox.find('ymax').text)]
        objects.append(obj_struct)

    return objects

def rec_from_txt(filename):
    objects = []
           
    gts = open(filename).read().splitlines()
    for gt in gts:
        gt = gt.split(" ")
        # print(gt)
        obj_struct = {}
        obj_struct['name'] = gt[4]
        # print(obj_struct['name'])
        obj_struct['bbox'] = [int(gt[0])*3,
                              int(gt[1])*3,
                              int(gt[2])*3,
                              int(gt[3])*3]
        # obj_struct['plate']= gt[5:]
        # print(gt[5:])
        objects.append(obj_struct)
    # print(filename)
    # print(objects)
    return objects






def voc_ap(rec, prec, use_07_metric=False):
    """Compute VOC AP given precision and recall. If use_07_metric is true, uses
    the VOC 07 11-point method (default:False).
    """
    if use_07_metric:
        # 11 point metric
        ap = 0.
        for t in np.arange(0., 1.1, 0.1):
            if np.sum(rec >= t) == 0:
                p = 0
            else:
                p = np.max(prec[rec >= t])
            ap = ap + p / 11.
    else:
        # correct AP calculation
        # first append sentinel values at the end
        mrec = np.concatenate(([0.], rec, [1.]))
        
        mpre = np.concatenate(([0.], prec, [0.]))

        # compute the precision envelope
        for i in range(mpre.size - 1, 0, -1):
            mpre[i - 1] = np.maximum(mpre[i - 1], mpre[i])

        # to calculate area under PR curve, look for points
        # where X axis (recall) changes value
        i = np.where(mrec[1:] != mrec[:-1])[0]

        # and sum (\Delta recall) * prec
        ap = np.sum((mrec[i + 1] - mrec[i]) * mpre[i + 1])
    return ap


def voc_eval(detpath,
             annopath,
            #  imagesetfile,
             classname,
             cachedir,
             ovthresh=0.5,
             use_07_metric=False):
    """rec, prec, ap = voc_eval(detpath,
                                annopath,
                                imagesetfile,
                                classname,
                                [ovthresh],
                                [use_07_metric])
    Top level function that does the PASCAL VOC evaluation.
    detpath: Path to detections
        detpath.format(classname) should produce the detection results file.
    annopath: Path to annotations
        annopath.format(imagename) should be the xml annotations file.
    imagesetfile: Text file containing the list of images, one image per line.
    classname: Category name (duh)
    cachedir: Directory for caching the annotations
    [ovthresh]: Overlap threshold (default = 0.5)
    [use_07_metric]: Whether to use VOC07's 11 point AP computation
        (default False)
    """
    # assumes detections are in detpath.format(classname)
    # assumes annotations are in annopath.format(imagename)
    # assumes imagesetfile is a text file with each line an image name
    # cachedir caches the annotations in a pickle file

    # first load gt
    if not os.path.isdir(cachedir):
        os.mkdir(cachedir)
    # imageset = os.path.splitext(os.path.basename(imagesetfile))[0]
    cachefile = os.path.join(cachedir, 'face.pkl')
    # read list of images
    # with open(imagesetfile, 'r') as f:
    #     lines = f.readlines()
    # imagenames = [x.strip() for x in lines]
    # imagenames = os.listdir(imagesetfile)
    imagenames = os.listdir(annopath)
    # print(imagenames)


    if not os.path.isfile(cachefile):
        # load annots
        recs = {}
        for i, imagename in enumerate(imagenames):
            # print(imagename)
            imagename = imagename.replace(".txt","")
            # print(imagename)
            # recs[imagename] = parse_rec(os.path.join(annopath,imagename)+'.txt')
            recs[imagename] = rec_from_txt(os.path.join(annopath,imagename)+'.txt')
            # print(recs)
            if i % 100 == 0:
                logger.info(
                    'Reading annotation for {:d}/{:d}'.format(
                        i + 1, len(imagenames)))
        # save
        logger.info('Saving cached annotations to {:s}'.format(cachefile))
        # print(recs)
        with open(cachefile, 'wb') as f:
            pickle.dump(recs, f)
    else:
        # load
        with open(cachefile, 'rb') as f:
            recs = pickle.load(f)
        # print(recs)

    # extract gt objects for this class
    class_recs = {}
    npos = 0
    for imagename in imagenames:
        imagename = imagename.replace(".txt","")
        # print(imagename)
        # print(recs)
        
        R = [obj for obj in recs[imagename] if obj['name'] == classname]
        # print(len(R))
        bbox = np.array([x['bbox'] for x in R])
        # plate_l = np.array([x['plate'] for x in R])

        # print(imagename)
        # print(R)
        # difficult = np.array([0 for x in R]).astype(np.bool)
        det = [False] * len(R)
        npos = npos + len(R)
        # print(npos)
        class_recs[imagename] = {'bbox': bbox,
                                #  'plate': plate_l,
                                #  'difficult': difficult,
                                 'det': det}

    # read dets
    # detfile = detpath.format(classname)
    # with open(detfile, 'r') as f:
    #     lines = f.readlines()
    print(npos)
    # splitlines = [x.strip().split(' ') for x in lines]
    # image_ids = [x[0] for x in splitlines]
    # confidence = np.array([float(x[1]) for x in splitlines])
    # BB = np.array([[float(z) for z in x[1:]] for x in splitlines])

    detfile = os.listdir(detpath)
    image_ids = []
    confidence = []
    BB = []
    plate = []
    # BB2 = []
    for file in detfile:
        file_loc = os.path.join(det_path,file)
        with open(file_loc,'r') as f:
            # rlines = f.readlines()
            # lines = rlines[2:]
            lines = f.readlines()
        # image_ids.append
        # BB1 = []
        for line in lines[2:]:
            # print(line)
            line = line.split(" ")
            # print(line)
            # if line[0] == "0":
            if float(line[4])>0.9:
                image_ids.append(file.replace(".txt",""))
                    # confidence.append(float(line[5].strip()))
                confidence.append(float(line[4]))
                # print(confidence)
                BB.append([float(z) for z in line[0:4]])
            # print(BB)
            else:
                continue
            # plate.append(line[5:])
            # BB1=np.array([float(z) for z in line[0:4]])
        # print(BB1)
        # BB2.append(BB1)
    # print(BB2)
    
    BB = np.array(BB)
    # print(BB)
    confidence = np.array(confidence)
    # plate = np.array(plate)
    # print(plate)
    # print(confidence)




    # sort by confidence
    sorted_ind = np.argsort(-confidence)
    BB = BB[sorted_ind, :]
    # plate = plate[sorted_ind,:]
    image_ids = [image_ids[x] for x in sorted_ind]
    # print(image_ids)

    # go down dets and mark TPs and FPs
    nd = len(image_ids)
    # print(nd)
    warn = 0
    yes = 0
    tp = np.zeros(nd)
    fp = np.zeros(nd)
    for d in range(nd):
        # print(image_ids)
        try:
            R = class_recs[image_ids[d]]#label
            # print(R)
        except:
            warn+=1
            continue
        # print(image_ids[d])
        # print(BB)
        bb = BB[d, :].astype(float)
        ovmax = -np.inf
        BBGT = R['bbox'].astype(float)
        # label = R['plate']
        # label2 = plate[d,:]
        # if label[0]==label2:
        #     yes +=1
        # else:
        # print(image_ids[d])
        # print(BBGT)
        # print(bb)
        

        if BBGT.size > 0:
            # compute overlaps
            # intersection
            ixmin = np.maximum(BBGT[:, 0], bb[0])
            iymin = np.maximum(BBGT[:, 1], bb[1])
            ixmax = np.minimum(BBGT[:, 2], bb[2])
            iymax = np.minimum(BBGT[:, 3], bb[3])
            iw = np.maximum(ixmax - ixmin + 1., 0.)
            ih = np.maximum(iymax - iymin + 1., 0.)
            inters = iw * ih

            # union
            uni = ((bb[2] - bb[0] + 1.) * (bb[3] - bb[1] + 1.) +
                   (BBGT[:, 2] - BBGT[:, 0] + 1.) *
                   (BBGT[:, 3] - BBGT[:, 1] + 1.) - inters)

            overlaps = inters / uni
            ovmax = np.max(overlaps)
            jmax = np.argmax(overlaps)
            # print(ovmax)


        if ovmax > ovthresh:
            # print("aaa")
            if not R['det'][jmax]:
                tp[d] = 1.
                R['det'][jmax] = 1
            else:
                fp[d] = 1.
        else:
            fp[d] = 1.
            # print(image_ids[d])

    # compute precision recall
    # print(tp)
    # print(len(tp))
    print("yes",yes)
    print("warn",warn)
    fp = np.cumsum(fp)
    tp = np.cumsum(tp)
    print(tp[-1])
    print(tp[-1]+fp[-1])
    rec = tp/npos
    print(npos)
    # avoid divide by zero in case the first detection matches a difficult
    # ground truth
    # print(" ",np.maximum(tp + fp, np.finfo(np.float64).eps))
    prec = tp / np.maximum(tp + fp, np.finfo(np.float64).eps)
    ap = voc_ap(rec, prec, use_07_metric)

    return rec, prec, ap

if __name__ == '__main__':
    det_path = "D:\\datasets\\Face2\\face1600_txt\\"
    anno_path = "D:\\datasets\\Face2\\face0707L\\"
    cache_path = './'
    #格式要求：txt：首位为类别，接下来为四个坐标，最后放置信度
    rec,prec,ap = voc_eval(detpath=det_path,annopath=anno_path,classname="0",cachedir=cache_path,ovthresh=0.5)
    
    print("recall:  ",rec[-1])
    print("precision:  ",prec[-1])
    print("ap:  ",ap)
