#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
A close_tour_update, marks the user as having already received tour in user.json received_tours
"""

from mitosheet.mito_analytics import identify
from mitosheet.user.user_utils import get_user_field, set_user_field


CLOSE_TOUR_EVENT = 'close_tour_update'
CLOSE_TOUR_PARAMS = ['received_tour']


def execute_close_tour_update(wsc, received_tour):
    """
    The function responsible for registering that the user took a specific tour in the user.json.
    """
    # Check which tours they have already completed
    received_tours = get_user_field('received_tours')
    if received_tours == None: 
        received_tours = []
    
    # If the tour they took is not already part of their received_tours list
    if received_tour not in received_tours:
        received_tours.append(received_tour)
    
    # Set their received tour
    set_user_field('received_tours', received_tours)


CLOSE_TOUR_UPDATE = {
    'event_type': CLOSE_TOUR_EVENT,
    'params': CLOSE_TOUR_PARAMS,
    'execute': execute_close_tour_update
}