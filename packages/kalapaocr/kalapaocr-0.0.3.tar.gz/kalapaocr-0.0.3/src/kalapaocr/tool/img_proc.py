import numpy as np
import cv2

def find_cc_in_thresh_image(thresh_image):
    stats= cv2.connectedComponentsWithStats(thresh_image, 4, cv2.CV_32S)[2][1:]
    return stats[stats[:, 0].argsort()]

def bgr2thresh(bgr_image):
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
    _, thresh = cv2.threshold(
        gray_image, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return thresh

def is_w_line(line_image,i):
    height, _ = line_image.shape
    stats = find_cc_in_thresh_image(line_image)
    for stat in stats:
        if stat[3] > 0.9 * height: #h
            return True
    return False

def find_and_remove_w_line(thresh_cc_image, w_region=5):
    _, width = thresh_cc_image.shape
    start_id = None
    end_id = None
    list_start_id = []
    list_end_id = []
    width_of_line = 0
    max_width_of_line = 0
    for i in range(0, width):
        end_check = min(i+w_region, width)
        if is_w_line(thresh_cc_image[:, i: end_check],i):
            pos_y, _ = np.where(thresh_cc_image[:, i: end_check] > 0)
            min_y, max_y = np.min(pos_y), np.max(pos_y)
            for j in range(i, end_check):
                if thresh_cc_image[min_y, j] > 0 or thresh_cc_image[max_y, j] > 0:
                    start_id = j
                    list_start_id.append(j)
                    break
            for j in range(end_check-1, i-1, -1):
                if thresh_cc_image[min_y, j] > 0 or thresh_cc_image[max_y, j] > 0:
                    end_id = j
                    list_end_id.append(j)
                    break
        if start_id != None and end_id != None:
            width_of_line = end_id - start_id
            max_width_of_line = max(max_width_of_line, width_of_line)
    if len(list_start_id) > 0:
        if max_width_of_line == 1:
            max_width_of_line = min(max_width_of_line + 1, width)
        return list_start_id[0], max_width_of_line
    else:
        return None, 0


def rm_line_border(img_thresh):
    img = img_thresh.copy()
    height, width = img.shape
    if height >= 2. * width:
        return img

    erosion = cv2.dilate(img, kernel=np.ones((3, 10), np.uint8))
    if height > 100:
        check_h_size = 25
    else:
        check_h_size = 20

    if width/height >= 2.5:
        boxes = find_cc_in_thresh_image(erosion[:, 30: width - 30])
        for box in boxes:
            if len(box) == 0:
                continue
            x_min, y_min, w, h, area = box
            if w > width * 0.4 and h <= 20 and (y_min <= 20 or y_min >= height - 20):
                img[y_min:y_min+h, :] = 0

    erosion = cv2.dilate(img, kernel=np.ones((3, 10), np.uint8))
    boxes = find_cc_in_thresh_image(erosion)
    big_box = False
    for box in boxes:
        x_min, y_min, w, h, area = box
        if (w > width * 0.4 and h <= 20 and (y_min <= 20 or y_min >= height - 20)) and width/height >= 1.5:
            check_w_size = 25
        elif (w > width * 0.65 and h <= 15 and (y_min <= 15 or y_min >= height - 15)) and width/height < 1.5:
            check_w_size = width
        else:
            if width/height >= 1.5:
                check_w_size = 25
            else:
                check_w_size = width
            big_box = True

        if big_box == False:
            erosion[y_min:y_min+h, :] = 0
            img[y_min:y_min+h, :] = 0

        x_line, w_line = find_and_remove_w_line(
            erosion[:, :check_w_size], w_region=10)
        if x_line != None:
            erosion[:, x_line:x_line+w_line] = 0
            img[:, x_line:x_line+w_line] = 0

        img_flip = cv2.flip(img, 1)
        erosion_flip = cv2.flip(erosion, 1)
        x_line, w_line = find_and_remove_w_line(
            erosion_flip[:, :check_w_size], w_region=10)
        if x_line != None:
            img_flip[:, x_line:x_line+w_line] = 0
            erosion_flip[:, x_line:x_line+w_line] = 0
            img = cv2.flip(img_flip, 1)
            erosion = cv2.flip(img_flip, 1)
        if big_box == True:
            boxes = find_cc_in_thresh_image(erosion)
            for box in boxes:
                x_min, y_min, w, h, area = box
                if (((w > width * 0.4 and width/height >= 1.5) or (w > width * 0.65 and width/height < 1.5))
                        and h <= check_h_size and (y_min <= check_h_size or y_min >= height - check_h_size)):
                    img[y_min:y_min+h, :] = 0
                if (y_min <= 3 or y_min >= height - 3) and h > 0.9 * height and (x_min <= 5 or x_min >= width-5) and w <= 10 and width < height:
                    tmp = img.copy()
                    tmp[:, x_min:x_min+w] = 0
                    if np.sum(tmp[:, x_min:x_min+w]) < 10:
                        img = tmp.copy()
    return np.invert(img)

def check_pixel(white_bg_image, stats, img_shape):
    height, width = img_shape
    if np.sum(white_bg_image) > 0.99 * height * width * 255:
        if len(stats) == 1 and (stats[0][2] == 1 or stats[0][3] == 1):
            return True

    if np.sum(white_bg_image) > 0.98 * height * width * 255:
        if all([(stat[1] > 0.97 * height or stat[1] < 0.02 * height)
                and stat[3] < height // 20 for stat in stats]):
            return True

    if all([stat[2] < 0.1 * height and stat[3] < 0.1 * height
            and 0.5 < stat[3]/stat[2] < 2.0 for stat in stats]):
        return True

    if all([((stat[1] + stat[3] >= 0.8 * height or stat[0] == 0)
                and stat[3] < height * 0.2) or (stat[1] <= 0.1 * height
            and stat[3] < 0.4 * height) for stat in stats]) \
        and stats[-1][0] - stats[0][0] >= 0.6 * width \
            and len(stats) >= 5:
        return True

def check_small_dot_cases(invert_white_bg_image, stats):
    if (invert_white_bg_image.shape[0] >= 21) and (invert_white_bg_image.shape[1] >= 21):
        tmp_img = invert_white_bg_image.copy()[10:-10, 10:-10]
    else:
        tmp_img = invert_white_bg_image
    tmp_img = cv2.erode(tmp_img, np.ones((3, 3), np.uint8))
    vis = tmp_img.copy()
    for component in stats:
        x, y, w, h, _ = component
        if x < 10:
            w = w - x
        if y < 10:
            h = h - y
        if 1 <= w <= 15 and 1 <= h <= 15:
            x = max(x - 10, 0)
            y = max(y - 10, 0)
            tmp_img[y:y+h, x:x+w] = 0
            cv2.rectangle(vis, (x, y), (x+w, y+h),
                            color=(255, 255, 255), thickness=1)
    if np.sum(tmp_img) <= 2000:
        return True

def check_empty_second(white_bg_image):

    height, width = white_bg_image.shape
    if np.mean(white_bg_image) == 255:
        return True

    invert_white_bg_image = np.invert(white_bg_image)
    stats = find_cc_in_thresh_image(invert_white_bg_image)

    if check_pixel(white_bg_image, stats, (height, width)):
        return True

    if check_small_dot_cases(invert_white_bg_image, stats):
        return True

    return False

def is_empty_image(bgr):
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    
    if np.sum(gray) > (0.999 * bgr.shape[0] * bgr.shape[1] * 255):
        return True

    thresh = bgr2thresh(bgr)
    
    if np.sum(gray * thresh) > np.sum(thresh) * 240/255:
        if np.average(gray) > 245:
            return True

    # check white second mode
    check_image = rm_line_border(thresh)
    if check_empty_second(check_image): # it is white_bg !!!
        return True

    return False