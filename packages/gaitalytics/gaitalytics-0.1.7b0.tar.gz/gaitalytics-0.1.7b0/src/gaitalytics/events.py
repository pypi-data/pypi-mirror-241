from abc import ABC, abstractmethod
from types import MappingProxyType
from typing import List

import numpy as np
from btk import btkAcquisition, btkEvent, btkForcePlatformsExtractor, btkGroundReactionWrenchFilter
from matplotlib import pyplot as plt
from scipy import signal

import gaitalytics.c3d
import gaitalytics.utils

FORCE_PLATE_SIDE_MAPPING_CAREN = MappingProxyType({"Left": 0, "Right": 1})


# Event detection
class AbstractGaitEventDetector(ABC):

    @abstractmethod
    def detect_events(self, acq: btkAcquisition, **kwargs):
        pass

    @staticmethod
    def _create_event(acq, frame: int,
                      event_label: gaitalytics.utils.GaitEventLabel,
                      event_context: gaitalytics.utils.GaitEventContext):
        frequency = acq.GetPointFrequency()
        start_frame = acq.GetMetaData().GetChild("TRIAL").GetChild("ACTUAL_START_FIELD").GetInfo().ToInt()[0] - 1
        start_time = start_frame / frequency

        event = btkEvent()
        event.SetLabel(event_label.value)
     #   event.SetFrame(int(frame + start_frame))
        event.SetId(gaitalytics.utils.GaitEventLabel.get_type_id(event_label.value))
        event.SetContext(event_context.value)
        event.SetTime(float(((frame - 1) / frequency) + start_time))
        return event


class ZenisGaitEventDetector(AbstractGaitEventDetector):
    """
    This class detects gait events from cgm2 model data
    """

    def __init__(self, configs: gaitalytics.utils.ConfigProvider,
                 **kwargs):
        """ Initializes Object

        :param foot_strike_offset: numbers of frames to offset next foot strike event
        :param foot_off_offset: number of frames to offset next foot off event
        """
        self._config = configs
        self._foot_strike_offset = kwargs.get("foot_strike_offset", 0)
        self._foot_off_offset = kwargs.get("foot_off_offset", 0)

    def detect_events(self, acq: btkAcquisition, **kwargs):
        """detects zeni gait events and stores it in to the acquisition

        :param acq: loaded and filtered acquisition
        :param min_distance: minimum frames between same event
        :param show_plot: plots of zenis shown
        """
        min_distance = kwargs.get("min_distance", 100)
        show_plot = kwargs.get("show_plot", False)

        right_heel = acq.GetPoint(self._config.MARKER_MAPPING.right_heel.value).GetValues()[:,
                     gaitalytics.utils.AxesNames.y.value]
        left_heel = acq.GetPoint(self._config.MARKER_MAPPING.left_heel.value).GetValues()[:,
                    gaitalytics.utils.AxesNames.y.value]
        right_toe = acq.GetPoint(self._config.MARKER_MAPPING.right_meta_2.value).GetValues()[:,
                    gaitalytics.utils.AxesNames.y.value]
        left_toe = acq.GetPoint(self._config.MARKER_MAPPING.left_meta_2.value).GetValues()[:,
                   gaitalytics.utils.AxesNames.y.value]
        right_hip = acq.GetPoint(self._config.MARKER_MAPPING.right_back_hip.value).GetValues()[:,
                    gaitalytics.utils.AxesNames.y.value]
        left_hip = acq.GetPoint(self._config.MARKER_MAPPING.left_back_hip.value).GetValues()[:,
                   gaitalytics.utils.AxesNames.y.value]
        '''
        left_heel, left_toe, right_heel, right_toe, right_hip, left_hip = self._move_to_plus(left_heel,
                                                                                             left_hip,
                                                                                             left_toe,
                                                                                             right_heel,
                                                                                             right_hip,
                                                                                             right_toe)
        '''
        sacrum = (right_hip + left_hip) / 2.0
        right_diff_heel = (right_heel - sacrum) * -1
        left_diff_heel = (left_heel - sacrum) * -1
        right_diff_toe = right_toe - sacrum
        left_diff_toe = left_toe - sacrum

        if show_plot:
            base_title = "Test"
            self._plot_curves(right_diff_heel,
                              right_heel,
                              sacrum, f"{base_title}_right_heel")
            self._plot_curves(left_diff_heel,
                              left_heel,
                              sacrum, f"{base_title}_left_heel")

        self._create_events(acq, left_diff_toe, gaitalytics.utils.GaitEventLabel.FOOT_OFF,
                            gaitalytics.utils.GaitEventContext.LEFT, min_distance, show_plot)
        self._create_events(acq, right_diff_toe, gaitalytics.utils.GaitEventLabel.FOOT_OFF,
                            gaitalytics.utils.GaitEventContext.RIGHT, min_distance, show_plot)
        self._create_events(acq, left_diff_heel, gaitalytics.utils.GaitEventLabel.FOOT_STRIKE,
                            gaitalytics.utils.GaitEventContext.LEFT, min_distance, show_plot)
        self._create_events(acq, right_diff_heel, gaitalytics.utils.GaitEventLabel.FOOT_STRIKE,
                            gaitalytics.utils.GaitEventContext.RIGHT, min_distance, show_plot)

    @staticmethod
    def _plot_curves(diff, foot, sacrum, title):
        from_frame = 3000
        to_frame = 3500
        fig, host = plt.subplots(figsize=(15, 12), layout='constrained')
        diff_short = diff[from_frame:to_frame]
        foot_short = foot[from_frame:to_frame]
        sacrum_short = sacrum[from_frame:to_frame]

        ax2 = host.twinx()
        ax3 = host.twinx()

        host.set_xlabel("Time")
        host.set_ylabel("Diff")
        ax2.set_ylabel("foot")
        ax3.set_ylabel("sacrum")

        color1, color2, color3 = plt.cm.viridis([0, .5, .9])
        p1 = host.plot(diff_short, color=color1, label="diff")
        extremes, foo = signal.find_peaks(diff_short)
        host.plot(extremes, diff_short[extremes], "x")
        p2 = ax2.plot(foot_short, color=color2, label="foot")
        p3 = ax3.plot(sacrum_short, color=color3, label="sacrum")

        host.legend(handles=p1 + p2 + p3, loc='best')
        # right, left, top, bottom
        ax3.spines['right'].set_position(('outward', 60))
        plt.savefig(f"./playground/{title}.png")
        plt.show()

    @staticmethod
    def _move_to_plus(left_heel, left_hip, left_toe, right_heel, right_hip, right_toe):
        min_value = abs(min([min(right_heel),
                             min(right_toe),
                             min(left_heel),
                             min(left_toe),
                             min(right_hip),
                             min(left_hip)]))
        right_heel = right_heel + min_value
        left_heel = left_heel + min_value
        right_toe = right_toe + min_value
        left_toe = left_toe + min_value
        right_hip = right_hip + min_value
        left_hip = left_hip + min_value

        return left_heel, left_toe, right_heel, right_toe, right_hip, left_hip

    #   gaitalytics.c3d.sort_events(acq)

    def _create_events(self, acq, diff, event_label: gaitalytics.utils.GaitEventLabel,
                       event_context: gaitalytics.utils.GaitEventContext,
                       min_distance: int = 100,
                       show_plot: bool = False):
        data = diff
        if gaitalytics.c3d.is_progression_axes_flip(
                acq.GetPoint(self._config.MARKER_MAPPING.left_heel.value).GetValues(),
                acq.GetPoint(self._config.MARKER_MAPPING.left_meta_5.value).GetValues()):
            data = data * -1

        data = gaitalytics.utils.min_max_norm(data)

        extremes, foo = signal.find_peaks(data, height=[0, 1], distance=min_distance)

        # add offset
        if event_label == gaitalytics.utils.GaitEventLabel.FOOT_STRIKE:
            extremes = extremes + self._foot_strike_offset
        elif event_label == gaitalytics.utils.GaitEventLabel.FOOT_OFF:
            extremes = extremes + self._foot_off_offset

        for frame in extremes:
            acq.AppendEvent(self._create_event(acq, frame, event_label, event_context))


class ForcePlateEventDetection(AbstractGaitEventDetector):
    """
    This class detects gait events from Force Plate signals
    """

    def __init__(self, **kwargs):
        """
        Initializes Object
        :param mapped_force_plate: Dictionary with name of force plate and index
        :param force_gait_event_threshold: threshold in newton to define gait event
        """
        self._mapped_force_plate = kwargs.get("mapped_force_plate", FORCE_PLATE_SIDE_MAPPING_CAREN)
        self._weight_threshold = kwargs.get("force_gait_event_threshold", 150)

    def detect_events(self, acq: btkAcquisition, **kwargs):
        """
        Detect force plate gait events with peak detection
        :param acq: loaded and filtered acquisition
        """

        for context in gaitalytics.utils.GaitEventContext:
            force_down_sample = force_plate_down_sample(acq, self._mapped_force_plate[context.value])
            detection = detect_onset(force_down_sample, threshold=self._weight_threshold)
            sequence = self._detect_gait_event_type(force_down_sample, detection)
            self._store_force_plate_events(acq, context, sequence)

    def _store_force_plate_events(self, btk_acq, context, sequence):
        for elem in sequence:
            event_label = elem[0]
            frame = elem[1]
            ev = self._create_event(btk_acq, frame, event_label, context)
            btk_acq.AppendEvent(ev)

    @staticmethod
    def _detect_gait_event_type(force_plate_signal: list, detected_force_plate_events: np.ndarray) -> list:
        """
        Iterate through each event detected by detect_onset and determine if the event is a FootStrike or a FootOff.
        Return array of ["Type of event":str,index of event:int]
        :param force_plate_signal: Signal of the force plate
        :param detected_force_plate_events: detection from detect_onset
        :return: 2 dimensional array with event name and frame index
        """

        signal_length = len(force_plate_signal)
        detected_event_types = []
        for couple_index in detected_force_plate_events:
            for signal_index in couple_index:

                # check for index out of bound
                if 20 < signal_index < (signal_length - 20):

                    # positive or negative slope (FeetOff or FeetStrike)
                    diff = force_plate_signal[signal_index - 20] - force_plate_signal[signal_index + 20]
                    if diff > 0:
                        detected_event_types.append([gaitalytics.utils.GaitEventLabel.FOOT_OFF, signal_index])
                    else:
                        detected_event_types.append([gaitalytics.utils.GaitEventLabel.FOOT_STRIKE, signal_index])
        return detected_event_types  # Contain the label of the event and the corresponding index


# Anomaly detection
class GaitEventAnomaly:
    """
    Stores anomalies for easy print
    """

    def __init__(self, start_frame: int, end_frame: int, context: str, anomaly: str):
        self.start_frame = start_frame
        self.end_frame = end_frame
        self.context = context
        self.anomaly = anomaly

    def __str__(self):
        return f"{self.anomaly}: {self.start_frame} - {self.end_frame} ({self.context})"


class AbstractEventAnomalyChecker(ABC):
    """
    Queued Events anomaly checker framework. Calls checker in a defined sequence
    """

    def __init__(self, event_checker=None):
        """
        Initiate instance and adds event_checker as callable child.
        :param event_checker: Subclass of EventAnomalyChecker
        """
        self.child = event_checker

    def check_events(self, acq_walk: btkAcquisition) -> [bool, list]:
        """
        Calls event anomaly checker of subclass and its children in sequences
        :param acq_walk: Acquisition with predefined events
        """
        [anomaly_detected, abnormal_event_frames] = self._check_events(acq_walk)
        if self.child is not None:
            [child_anomaly_detected, child_abnormal_event_frames] = self.child.check_events(acq_walk)

            abnormal_event_frames.extend(child_abnormal_event_frames)
            anomaly_detected = child_anomaly_detected | anomaly_detected
        return anomaly_detected, abnormal_event_frames

    @abstractmethod
    def _check_events(self, acq_walk: btkAcquisition) -> [bool, List[GaitEventAnomaly]]:
        """
        Implementation of event checker
        :param acq_walk: Acquisition with added Events
        :return: flag is anomalies found, list of anomalies
        """
        pass


class ContextPatternChecker(AbstractEventAnomalyChecker):
    """
    Checks if events are alternating between Heel_Strike and Foot_Off per context
    """

    def _check_events(self, acq_walk: btkAcquisition) -> [bool, List[GaitEventAnomaly]]:
        """
        kick off the checker
        :param acq_walk: Acquisition with added Events
        :return: flag is anomalies found, list of anomalies
        """
        abnormal_event_frames = []
        anomaly_detected = False

        gaitalytics.c3d.sort_events(acq_walk)

        for current_event_index in range(0, acq_walk.GetEventNumber()):
            current_event = acq_walk.GetEvent(current_event_index)
            context = current_event.GetContext()
            for next_event_index in range(current_event_index + 1, acq_walk.GetEventNumber()):
                next_event = acq_walk.GetEvent(next_event_index)
                if next_event.GetContext() == context:
                    if current_event.GetLabel() == next_event.GetLabel():
                        anomaly_detected = True
                        anomaly = GaitEventAnomaly(current_event.GetFrame(),
                                                   next_event.GetFrame(), context,
                                                   f"Event sequence off")
                        abnormal_event_frames.append(anomaly)

                    break

        return [anomaly_detected, abnormal_event_frames]


class EventSpacingChecker(AbstractEventAnomalyChecker):

    def __init__(self, event_checker=None, frame_threshold=30):
        super().__init__(event_checker)
        self._frame_threshold = frame_threshold

    def _check_events(self, acq_walk: btkAcquisition) -> [bool, List[GaitEventAnomaly]]:
        anomaly_detected = False
        abnormal_event_frames = []
        for current_event_index in range(0, acq_walk.GetEventNumber()):
            current_event = acq_walk.GetEvent(current_event_index)
            context = current_event.GetContext()
            for next_event_index in range(current_event_index + 1, acq_walk.GetEventNumber()):
                next_event = acq_walk.GetEvent(next_event_index)
                if next_event.GetContext() == context:
                    if next_event.GetFrame() - current_event.GetFrame() < self._frame_threshold:
                        anomaly = GaitEventAnomaly(current_event.GetFrame(),
                                                   next_event.GetFrame(), context,
                                                   f"Spacing smaller than {self._frame_threshold}")
                        abnormal_event_frames.append(anomaly)
                        anomaly_detected = True
                    break
        return [anomaly_detected, abnormal_event_frames]


# utils
def find_next_event(acq: btkAcquisition, label: str, context, start_index: int) -> [btkEvent, List[btkEvent]]:
    if acq.GetEventNumber() >= start_index + 1:
        unused_events: List[btkEvent] = []
        for event_index in range(start_index + 1, acq.GetEventNumber()):
            event = acq.GetEvent(event_index)
            if event.GetContext() == context:
                if event.GetLabel() == label:
                    return [event, unused_events]

            unused_events.append(event)
    raise IndexError()


def force_plate_down_sample(acq: btkAcquisition, force_plate_index: int) -> list:
    """

    :param acq: c3d file
    :param force_plate_index: index of force plate in c3d
    :return: down sample data
    """
    first_frame_index = acq.GetFirstFrame()
    last_frame_index = acq.GetLastFrame()
    analog_sample_per_frame = acq.GetNumberAnalogSamplePerFrame()

    force_plate_extractor = btkForcePlatformsExtractor()
    ground_reaction_filter = btkGroundReactionWrenchFilter()

    force_plate_extractor.SetInput(acq)
    force_plate_collection = force_plate_extractor.GetOutput()
    ground_reaction_filter.SetInput(force_plate_collection)
    ground_reaction_collection = ground_reaction_filter.GetOutput()
    ground_reaction_collection.Update()
    force = ground_reaction_collection.GetItem(force_plate_index).GetForce().GetValues()
    return force[0:(last_frame_index - first_frame_index + 1) * analog_sample_per_frame:analog_sample_per_frame][:, 2]


def detect_onset(x, threshold=0, n_above=1, n_below=0,
                 threshold2=None, n_above2=1, show=False, ax=None):
    """Detects onset in data based on amplitude threshold.
    """
    ## TODO rewrite code, just copied it

    x = np.atleast_1d(x).astype('float64')
    # deal with NaN's (by definition, NaN's are not greater than threshold)
    x[np.isnan(x)] = -np.inf
    # indices of data greater than or equal to threshold
    inds = np.nonzero(x >= threshold)[0]
    if inds.size:
        # initial and final indexes of almost continuous data
        inds = np.vstack((inds[np.diff(np.hstack((-np.inf, inds))) > n_below + 1],
                          inds[np.diff(np.hstack((inds, np.inf))) > n_below + 1])).T
        # indexes of almost continuous data longer than or equal to n_above
        inds = inds[inds[:, 1] - inds[:, 0] >= n_above - 1, :]
        # minimum amplitude of n_above2 values in x to detect
        if threshold2 is not None and inds.size:
            idel = np.ones(inds.shape[0], dtype=bool)
            for i in range(inds.shape[0]):
                if np.count_nonzero(x[inds[i, 0]: inds[i, 1] + 1] >= threshold2) < n_above2:
                    idel[i] = False
            inds = inds[idel, :]
    if not inds.size:
        inds = np.array([])  # standardize inds shape for output

    return inds


def return_max_length(arrays):
    return len(max(arrays, key=len))


def tolerant_mean(arrs):
    lens = [len(i) for i in arrs]
    arr = np.ma.empty((np.max(lens), len(arrs)))
    arr.mask = True
    for idx, l in enumerate(arrs):
        arr[:len(l), idx] = l
    return arr.mean(axis=-1), arr.std(axis=-1)


def create_matrix_padded(matrix, max_length):
    matx = []
    lin_array = len(np.shape(matrix[0])) == 1
    for array in matrix:
        to_pad = max_length - len(array)
        if lin_array:
            array_pad = np.pad(array, (0, to_pad), 'constant', constant_values=0)
        else:
            array_pad = np.pad(array[:, 0], (0, to_pad), 'constant', constant_values=0)
        matx.append(array_pad)
    return matx
