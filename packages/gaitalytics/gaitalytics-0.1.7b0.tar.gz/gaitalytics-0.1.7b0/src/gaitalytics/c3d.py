from statistics import mean

import btk
import numpy as np

import gaitalytics.utils

ANALOG_VOLTAGE_PREFIX_LABEL = "Voltage."


def sort_events(acq):
    """
    sort events in acquisition

    Args:
        acq (btkAcquisition): a btk acquisition instance

    """
    events = acq.GetEvents()

    value_frame = {}
    for event in btk.Iterate(events):
        if event.GetFrame() not in value_frame:
            value_frame[event.GetFrame()] = event

    sorted_keys = sorted(value_frame)

    newEvents = btk.btkEventCollection()
    for key in sorted_keys:
        newEvents.InsertItem(value_frame[key])

    acq.ClearEvents()
    acq.SetEvents(newEvents)


def read_btk(filename):
    """
    read a c3d with btk

    Args:
        filename (str): filename with its path
    """
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(filename)
    reader.Update()
    acq = reader.GetOutput()

    # sort events
    sort_events(acq)

    return acq


def write_btk(acq, filename):
    """
    write a c3d with Btk

    Args:
        acq (btk.acquisition): a btk acquisition instance
        filename (str): filename with its path
    """
    writer = btk.btkAcquisitionFileWriter()
    writer.SetInput(acq)
    writer.SetFilename(filename)
    writer.Update()


def is_progression_axes_flip(left_heel, left_toe):
    return 0 < mean(left_toe[gaitalytics.utils.AxesNames.y.value] - left_heel[gaitalytics.utils.AxesNames.y.value])


# def correct_points_frame_by_frame(acq_trial: btk.btkAcquisition):
#     frame_size = acq_trial.GetPointFrameNumber()
#     correction = get_fastest_point_by_frame(acq_trial, 1)
#     for frame_number in range(1, frame_size):
#         if (frame_number + 2) < frame_size:
#             correction_new = get_fastest_point_by_frame(acq_trial, frame_number + 1)
#         correct_points_in_frame(acq_trial, frame_number, correction)
#         correction += correction_new


def correct_points_in_frame(acq_trial: btk.btkAcquisition, frame_number: int, correction: float):
    print(f"{frame_number}:{correction}")
    for point_number in range(0, acq_trial.GetPointNumber()):
        acq_trial.GetPoint(point_number).SetValue(frame_number, 1,
                                                  (acq_trial.GetPoint(point_number).GetValue(frame_number,
                                                                                             1) + correction))


def get_fastest_point_by_frame(acq_trial, frame_number) -> float:
    rfmh_point = acq_trial.GetPoint("RFMH")
    rhee_point = acq_trial.GetPoint("RHEE")
    lfmh_point = acq_trial.GetPoint("LFMH")
    lhee_point = acq_trial.GetPoint("LHEE")
    lfmh_dist = lfmh_point.GetValue(frame_number - 1, 1) - lfmh_point.GetValue(frame_number, 1)
    lhee_dist = lhee_point.GetValue(frame_number - 1, 1) - lhee_point.GetValue(frame_number, 1)
    rfmh_dist = rfmh_point.GetValue(frame_number - 1, 1) - rfmh_point.GetValue(frame_number, 1)
    rhee_dist = rhee_point.GetValue(frame_number - 1, 1) - rhee_point.GetValue(frame_number, 1)
    return np.min([lfmh_dist, lhee_dist, rfmh_dist, rhee_dist])


