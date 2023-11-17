import cv2
import numpy as np
from scipy import ndimage
import time


class Detector:
    def __init__(self, config=None, reflection_fill_color_index=0, gaussian_blur=True, binary_fill_hole=True):
        if reflection_fill_color_index is False or reflection_fill_color_index is None:
            self.reflection_fill = False
            self.reflection_fill_color_index = None
        else:
            if type(reflection_fill_color_index) is int and 0 <= reflection_fill_color_index <= 255:
                self.reflection_fill = True
                self.reflection_fill_color_index = reflection_fill_color_index
            else:
                self.reflection_fill = False
                self.reflection_fill_color_index = None
                raise ValueError("Reflection fill input must be integer type and must be between 0 and 255.")
        if type(gaussian_blur) is bool:
            self.gaussian_blur = gaussian_blur
        else:
            self.gaussian_blur = True
            raise ValueError("Gaussian blur input must be boolean type.")
        if type(binary_fill_hole) is bool:
            self.binary_fill_hole = binary_fill_hole
        else:
            self.binary_fill_hole = True
            raise ValueError("Binary fill hole input must be boolean type.")
        if config is not None:
            if type(config) is not dict:
                raise ValueError("The config input must be dictionary type.")
            else:
                for key, value in config.items():
                    self.update_config_by_name(key, value)
        else:
            self.min_circular_ratio = 0.9
            self.max_circular_ratio = 1.9
            self.ksize_height = 13
            self.ksize_width = 13
            self.min_binary_threshold = 20
            self.max_binary_threshold = 255
            self.reflection_fill_dilation_index = 25
            self.reflection_fill_square_dimension = 200

    def update_config(self, config_dict_input):
        if type(config_dict_input) is not dict:
            raise ValueError("The config input must be dictionary type.")
        else:
            for key, value in config_dict_input.items():
                self.update_config_by_name(key, value)

    def update_config_by_name(self, attribute_name, attribute_value):
        if attribute_name == "min_circular_ratio":
            if type(attribute_value) is not float or type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be float or integer.")
            else:
                self.min_circular_ratio = round(float(attribute_value), 1)
        elif attribute_name == "max_circular_ratio":
            if type(attribute_value) is not float or type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be float or integer.")
            else:
                self.max_circular_ratio = round(float(attribute_value), 1)
        elif attribute_name == "ksize_height":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.ksize_height = attribute_value
        elif attribute_name == "ksize_width":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.ksize_width = attribute_value
        elif attribute_name == "min_binary_threshold":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.min_binary_threshold = attribute_value
        elif attribute_name == "max_binary_threshold":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.max_binary_threshold = attribute_value
        else:
            print(f"Detector attribute type {attribute_name} could not find in detector attributes.")

    def get_config_info(self):
        temp_dict = {}
        temp_dict["min_circular_ratio"] = self.min_circular_ratio
        temp_dict["max_circular_ratio"] = self.max_circular_ratio
        temp_dict["ksize_height"] = self.ksize_height
        temp_dict["ksize_width"] = self.ksize_width
        temp_dict["min_binary_threshold"] = self.min_binary_threshold
        temp_dict["max_binary_threshold"] = self.max_binary_threshold
        temp_dict["reflection_fill_dilation_index"] = self.reflection_fill_dilation_index
        temp_dict["reflection_fill_square_dimension"] = self.reflection_fill_square_dimension
        return temp_dict

    def detect(self, frame_input):
        frame_shape = frame_input.shape
        frame_width = frame_shape[1]
        frame_height = frame_shape[0]

        # Checking it is rbg/bgr image or not
        # If yes, then change to grayscale image
        if len(frame_shape) == 3:
            frame_input = cv2.cvtColor(frame_input, cv2.COLOR_BGR2GRAY)

        if self.reflection_fill:
            dilation_index = self.reflection_fill_dilation_index
            square_dimension = self.reflection_fill_square_dimension

            _, reflection_shape = cv2.threshold(frame_input, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            kernel = np.ones((dilation_index, dilation_index), np.uint8)

            dilated_reflection_shape = cv2.dilate(reflection_shape, kernel, iterations=1)

            hh, ww = dilated_reflection_shape.shape
            # shsp = square height start point, shep = square height end point
            shsp = int(hh / 2 - (square_dimension / 2))
            shep = int(hh / 2 + (square_dimension / 2))

            # shsp = square width start point, shep = square width end point
            swsp = int(ww / 2 - (square_dimension / 2))
            swep = int(ww / 2 + (square_dimension / 2))

            cropped_dilated_reflection_shape = dilated_reflection_shape[shsp:shep, swsp:swep]

            cloned_black_frame = np.copy(frame_input)
            cloned_black_frame.fill(0)
            cloned_black_frame[shsp:shep, swsp:swep] = cropped_dilated_reflection_shape

            reflection_shape_index = list(zip(*np.where(cloned_black_frame == 255)))

            # fill black color in pupil reflection area
            for position in reflection_shape_index:
                frame_input[position[0], position[1]] = 0

        if self.gaussian_blur:
            frame_input = cv2.GaussianBlur(frame_input, (self.ksize_height, self.ksize_width), 0)

        _, black_white_filter_frame = cv2.threshold(frame_input,
                                                    self.min_binary_threshold,
                                                    self.max_binary_threshold,
                                                    cv2.THRESH_BINARY_INV)

        if self.binary_fill_hole:
            binary_filled_frame = ndimage.binary_fill_holes(black_white_filter_frame).astype(np.uint8)
            binary_filled_frame[binary_filled_frame == 1] = 255
            try:
                contours, _ = cv2.findContours(binary_filled_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            except ValueError:
                contours = None
        else:
            try:
                contours, _ = cv2.findContours(black_white_filter_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            except ValueError:
                contours = None

        if contours is not None:
            contours = sorted(contours, key=lambda xx: cv2.contourArea(xx), reverse=True)

            min_circular_ratio = self.min_circular_ratio
            max_circular_ratio = self.max_circular_ratio
            largest_dia = 0.0
            largest_con_ind = 0
            error_string = None
            center_of_pupil = (0.0, 0.0)
            reversed_center_of_pupil = (0.0, 0.0)
            axes_of_pupil = (0.0, 0.0)
            average_diameter_of_pupil = 0.0
            angle_of_pupil = 0.0
            circular_con_count = 0
            for ind, cc in enumerate(contours):
                try:
                    (x, y), (MA, ma), angle = cv2.fitEllipse(cc)
                    con_ratio = ma / MA
                    # print(con_ratio)
                    if min_circular_ratio <= con_ratio <= max_circular_ratio:
                        avg_dia = (ma + MA) / 2
                        if avg_dia >= largest_dia:
                            largest_dia = avg_dia
                            largest_con_ind = ind
                            center_of_pupil = (float(x), float(y))
                            reversed_center_of_pupil = (float(frame_width - x), float(frame_height - y))
                            axes_of_pupil = (float(MA / 2), float(ma / 2))
                            average_diameter_of_pupil = avg_dia
                            angle_of_pupil = float(angle)
                            circular_con_count += 1
                except Exception as e:
                    error_string = str(e)
                    pass

            try:
                largest_circle = contours[largest_con_ind]
            except IndexError:
                largest_circle = None

            if largest_circle is not None:
                temp_dict = {}
                temp_dict["detector_timestamp"] = time.time()
                temp_dict["center_of_pupil"] = center_of_pupil
                temp_dict["reversed_center_of_pupil"] = reversed_center_of_pupil
                temp_dict["axes_of_pupil"] = axes_of_pupil
                temp_dict["angle_of_pupil"] = angle_of_pupil
                temp_dict["average_diameter_of_pupil"] = average_diameter_of_pupil
                return temp_dict
            else:
                temp_dict = {}
                temp_dict["detector_timestamp"] = time.time()
                temp_dict["center_of_pupil"] = (0.0, 0.0)
                temp_dict["reversed_center_of_pupil"] = (0.0, 0.0)
                temp_dict["axes_of_pupil"] = (0.0, 0.0)
                temp_dict["angle_of_pupil"] = 0.0
                temp_dict["average_diameter_of_pupil"] = 0.0
                return temp_dict
        else:
            temp_dict = {}
            temp_dict["detector_timestamp"] = time.time()
            temp_dict["center_of_pupil"] = (0.0, 0.0)
            temp_dict["reversed_center_of_pupil"] = (0.0, 0.0)
            temp_dict["axes_of_pupil"] = (0.0, 0.0)
            temp_dict["angle_of_pupil"] = 0.0
            temp_dict["average_diameter_of_pupil"] = 0.0
            return temp_dict
