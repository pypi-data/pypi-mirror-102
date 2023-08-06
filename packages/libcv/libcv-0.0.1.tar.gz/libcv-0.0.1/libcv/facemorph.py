import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


class FM(object):
    def __init__(self, mean_pts):
        self.mean_pts = mean_pts  # tuple list of (x, y)

    # Check if a point is inside a rectangle
    @staticmethod
    def _rect_contains(rect, point):
        if point[0] < rect[0]:
            return False
        elif point[1] < rect[1]:
            return False
        elif point[0] > rect[2]:
            return False
        elif point[1] > rect[3]:
            return False
        return True

    # Draw a point
    @staticmethod
    def draw_point(img, p, color):
        cv2.circle(img, p, 2, color, -1, cv2.LINE_AA, 0)

    # Draw delaunay triangles
    @staticmethod
    def draw_delaunay(img, triangleList, delaunay_color):
        size = img.shape
        r = (0, 0, size[1], size[0])

        for t in triangleList:

            pt1 = (t[0], t[1])
            pt2 = (t[2], t[3])
            pt3 = (t[4], t[5])

            if FM._rect_contains(r, pt1) and FM._rect_contains(
                    r, pt2) and FM._rect_contains(r, pt3):
                cv2.line(img, pt1, pt2, delaunay_color, 1, cv2.LINE_AA, 0)
                cv2.line(img, pt2, pt3, delaunay_color, 1, cv2.LINE_AA, 0)
                cv2.line(img, pt3, pt1, delaunay_color, 1, cv2.LINE_AA, 0)

    # save triangle points
    @staticmethod
    def save_tri_txt(path, tri_list):
        with open(path, 'w') as f:
            for tri in tri_list:
                line = ' '.join(tri)
                f.write(line + '\n')

    # Read in the points from a text file
    @staticmethod
    def read_points(path, size=None):
        points = []
        with open(path) as file:
            for line in file:
                x, y = line.split()
                if size is not None:
                    points.append((int(float(x) * size), int(float(y) * size)))
                else:
                    points.append((int(float(x)), int(float(y))))
        return points

    # change numpy array of [-1 , 2] to tuple list
    @staticmethod
    def array2tuple(pts):
        points = []
        for pt in pts:
            points.append((min(max(int(pt[0]), 0), 127),
                           min(max(int(pt[1]), 0), 127)))
        return points

    # get triangle list from points
    # the triangle order are random...
    @staticmethod
    def tri_from_pts(pts, rect):
        pts = FM._append_ext_pts(pts, rect)
        subdiv = cv2.Subdiv2D(rect)
        for p in pts:
            subdiv.insert(p)
        return subdiv.getTriangleList()

    @staticmethod
    def _append_ext_pts(pts, rect):
        # rect[3] is H , rect[2] is W
        pts.append((0, 0))
        pts.append((0, (rect[3] - 1) / 2))
        pts.append((0, rect[3] - 1))
        pts.append(((rect[2] - 1) / 2, rect[3] - 1))
        pts.append((rect[2] - 1, rect[3] - 1))
        pts.append(((rect[2] - 1), (rect[3] - 1) / 2))
        pts.append((rect[2] - 1, 0))
        pts.append(((rect[2] - 1) / 2, 0))

        return pts

    # get trianle list from hand craft
    @staticmethod
    def save_tri_index(tri_list, point_list, path='tri_order.txt'):
        '''
        tri_list : [(x1 , y1) , (x2 , y2) , (x3 , y3)] , len == 3
        point_list: [(x1 , y1) , (x2 , y2) ... ]
        
        * save to path as txt
        '''
        with open(path, 'w') as f:
            for tri in tri_list:

                def _get_index(pt):
                    min_dis = 1000
                    idx = -1
                    for i, p in enumerate(point_list):
                        dis = (p[0] - pt[0])**2 + (p[1] - pt[1])**2
                        if dis < min_dis:
                            min_dis = dis
                            idx = i
                    return idx

                line = ' '.join([str(_get_index(x)) for x in tri])
                f.write(line + '\n')

    # Apply affine transform calculated using srcTri and dstTri to src and
    # output an image of size.
    @staticmethod
    def applyAffineTransform(src, srcTri, dstTri, size):

        # Given a pair of triangles, find the affine transform.
        warpMat = cv2.getAffineTransform(
            np.float32(srcTri), np.float32(dstTri))

        # Apply the Affine Transform just found to the src image
        dst = cv2.warpAffine(
            src,
            warpMat, (size[0], size[1]),
            None,
            flags=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_REFLECT_101)

        return dst

    # Warps and alpha blends triangular regions from img1 and img2 to img
    @staticmethod
    def morphTriangle(img, t_1, t_2, rec_img):

        # Find bounding rectangle for each triangle
        r1 = cv2.boundingRect(np.float32([t_1]))
        r2 = cv2.boundingRect(np.float32([t_2]))
        # Offset points by left top corner of the respective rectangles
        t1Rect = []
        t2Rect = []

        for i in range(0, 3):
            t2Rect.append(((t_2[i][0] - r2[0]), (t_2[i][1] - r2[1])))
            t1Rect.append(((t_1[i][0] - r1[0]), (t_1[i][1] - r1[1])))

        # Get mask by filling triangle
        mask = np.zeros((r2[3], r2[2], 3), dtype=np.float32)
        cv2.fillConvexPoly(mask, np.int32(t2Rect), (1.0, 1.0, 1.0), 16, 0)

        # Apply warpImage to small rectangular patches
        imgRect = img[r1[1]:r1[1] + r1[3], r1[0]:r1[0] + r1[2]]

        size = (r2[2], r2[3])
        imgRect = FM.applyAffineTransform(imgRect, t1Rect, t2Rect, size)
        # Copy triangular region of the rectangular patch to the output image
        rec_img[r2[1]:r2[1] + r2[3], r2[0]:r2[0] +
                r2[2]] = rec_img[r2[1]:r2[1] + r2[3], r2[0]:r2[0] + r2[2]] * (
                    1 - mask) + imgRect * mask

    # morph face given points_1 , points_2 and ori image
    @staticmethod
    def faceMorph(img, pts_1, pts_2, tri_order_txt, viz=False):
        '''
        img : image to be warped
        pts_1 : from points
        pts_2 : to points with same order to pts_1
        tri_order_txt : txt with every line indice three points
        '''
        img = np.float32(img)
        rect = (0, 0, img.shape[1], img.shape[0])
        pts_1 = FM._append_ext_pts(pts_1, rect)
        pts_2 = FM._append_ext_pts(pts_2, rect)

        img_morph = 255 * np.ones((128, 128, 3), dtype=img.dtype)
        img_morph_viz = 255 * np.zeros((128 * 4, 128 * 4, 3), dtype=np.uint8)
        tri_list = []

        with open(tri_order_txt) as f:
            for line in f:
                x, y, z = line.split()
                x = int(x)
                y = int(y)
                z = int(z)
                t1 = [pts_1[x], pts_1[y], pts_1[z]]
                t2 = [pts_2[x], pts_2[y], pts_2[z]]
                FM.morphTriangle(img, t1, t2, img_morph)

                # plt.imshow(img_morph.astype(np.uint8))
                # plt.show()

                tri_list.append([
                    int(pts_1[x][0]) * 4,
                    int(pts_1[x][1]) * 4,
                    int(pts_1[y][0]) * 4,
                    int(pts_1[y][1]) * 4,
                    int(pts_1[z][0]) * 4,
                    int(pts_1[z][1]) * 4
                ])
        if viz:
            FM.draw_delaunay(img_morph_viz, tri_list, (255, 255, 255))
        return img_morph, img_morph_viz


if __name__ == '__main__':

    # Define window names
    win_delaunay = "Delaunay Triangulation"
    # Define colors for drawing.
    delaunay_color = (255, 255, 255)

    # Read in the image.
    img = cv2.imread("example/input/000001.jpg")

    # Keep a copy around
    img_orig = img.copy()

    # Rectangle to be used with Subdiv2D
    size = img.shape
    rect = (0, 0, size[1], size[0])

    # Create an instance of Subdiv2D
    subdiv = cv2.Subdiv2D(rect)

    # Create an array of points.
    points = FM.read_points("example/output/000001.txt")
    # Insert points into subdiv
    tri_list = FM.tri_from_pts(points, rect)
    print(tri_list)
    FM.draw_delaunay(img_orig, tri_list, (255, 255, 255))
    cv2.imshow(win_delaunay, img_orig)
    cv2.waitKey(100000)