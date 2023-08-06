// Copyright (c) Mito
// Distributed under the terms of the Modified BSD License.


import React, { Fragment, useEffect, useState } from 'react';

// Import css
import "../../../css/tour.css"
import { MitoAPI } from '../../api';
import XIcon from '../icons/XIcon';

// Location to display the TourStep popup
enum TourPopupLocation {
    BOTTOM_LEFT = 'bottom_left',
    BOTTOM_RIGHT = 'bottom-right'
}

type TourStep = {
    overlay: boolean,
    stepHeader: string,
    stepHeaderBackgroundColor: string,
    stepText: JSX.Element,
    location: TourPopupLocation,
    advanceButtonText: JSX.Element,
    displayBackButton: boolean
}

const steps: TourStep[] = [
    {
        overlay: false,
        stepHeader: 'Analyses in the Sidebar',
        stepHeaderBackgroundColor: '#BCDFBC',
        stepText: <div> With Mito&apos;s sidebars, it&apos;s easy to perform powerful analyses, like creating pivot tables, merging dataframes, and filtering your data. <b> Click on the pivot table button to get started</b>. </div>,
        location: TourPopupLocation.BOTTOM_LEFT,
        advanceButtonText: <Fragment>Continue &rarr;</Fragment>,
        displayBackButton: false,
    },
    {
        overlay: false,
        stepHeader: 'Create a Pivot Table',
        stepHeaderBackgroundColor: '#DDA1A1',
        stepText: <div> In the open sidebar, <b>select a row and value </b> to create your pivot table. Pivot tables group your data by the selected rows and columns, and then aggregate the values. </div>,
        location: TourPopupLocation.BOTTOM_LEFT,
        advanceButtonText: <Fragment>Continue &rarr;</Fragment>,
        displayBackButton: true
    },
    {
        overlay: false,
        stepHeader: 'That was easy!',
        stepHeaderBackgroundColor: '#79C2F8',
        stepText: <div>Each time you make an edit in Mito, the equivalent pandas code is generated below the Mito sheet. <b>Checkout the pivot table code below</b>. We just saved our first trip to stack overflow :&#x29; </div>,
        location: TourPopupLocation.BOTTOM_LEFT,
        advanceButtonText: <Fragment>Continue &rarr;</Fragment>,
        displayBackButton: true
    },
    {
        overlay: false,
        stepHeader: 'See the full tutorial',
        stepHeaderBackgroundColor: '#FFDAAE',
        stepText: <div>Clean and analyze your data by writing spreadsheet formulas, visualizing your data, and adding filters. Find a more detailed tutorial <a href="https://docs.trymito.io/getting-started/tutorial" target="_blank" rel="noreferrer" style={{color:'#0081DE'}}>here</a>.</div>,
        location: TourPopupLocation.BOTTOM_RIGHT,
        advanceButtonText: <Fragment>Close</Fragment>,
        displayBackButton: true
    }
]

const Tour = (props: {
    mitoAPI: MitoAPI;
    setHighlightPivotTableButton: (highlight: boolean) => void;
}): JSX.Element => {
    const [stepNumber, setStepNumber] = useState<number>(0)
    
    // Watch for step changes and update the highlighting of the pivot table button.
    useEffect(() => {
        if (stepNumber === 0) {
            props.setHighlightPivotTableButton(true)
            void props.mitoAPI.sendLogMessage(
                'begin_tour',
                {}
            )
        } else {
            props.setHighlightPivotTableButton(false)
        }
    }, [stepNumber])

    // Go to stepNumber if it exists, otherwise close the tour
    const goToStep = (newStepNumber: number) => {
        // Log switching steps
        void props.mitoAPI.sendLogMessage(
            'switched_tour_step',
            {
                'old_tour_step': stepNumber,
                'new_tour_step': newStepNumber
            }
        )

        if (newStepNumber < steps.length) {
            setStepNumber(newStepNumber)
        } else {
            void closeTour('pivot_tour');
        }
    }

    const closeTour = async (tourName: string): Promise<void> => {
        // Log closing the tour
        if (stepNumber >= steps.length - 1) {
            void props.mitoAPI.sendLogMessage(
                'finished_tour'
            ) 
        } else {
            void props.mitoAPI.sendLogMessage(
                'closed_tour_early'
            )
        }
        
        // Make sure that the pivot button is not stuck in pulsing mode. 
        props.setHighlightPivotTableButton(false)

        // Send the closeTour message to the backend
        await props.mitoAPI.sendCloseTour(tourName);
    }

    const progressBarDots: JSX.Element[] = []
    steps.forEach((step, index) => {
        // Determine if the dot should be small or large
        const diameterClassName = index === stepNumber ? 'tour-progress-bar-dot  large-dot' : 'tour-progress-bar-dot  small-dot';
        progressBarDots.push((
            <div className={diameterClassName} onClick={() => goToStep(index)}/>
        ))
    })

    // Get the location to display the tour as a className
    const tourContainerLocation = steps[stepNumber].location === TourPopupLocation.BOTTOM_LEFT ? 
        'tour-container tour-container-bottom-left' : 
        'tour-container tour-container-bottom-right'
    
    // If we're at a valid step number
    return (
        <div className={tourContainerLocation} key={stepNumber}>
            <div className='tour-header-container' style={{backgroundColor: steps[stepNumber].stepHeaderBackgroundColor}}>
                {steps[stepNumber].stepHeader}
                <div className='tour-header-close-button' onClick={() => closeTour('pivot_tour')}>
                    <XIcon/>
                </div>
            </div>
            <div className='tour-step-text-container'>
                {steps[stepNumber].stepText}
            </div>
            <div className='tour-button-container'>
                {steps[stepNumber].displayBackButton && 
                    <div className='tour-close-button' onClick={() => goToStep(stepNumber - 1)}>
                        Back
                    </div>
                }
                <div className='tour-continue-button' onClick={() => goToStep(stepNumber + 1)}>
                    {steps[stepNumber].advanceButtonText}
                </div>
            </div>
            <div className='tour-progress-bar-container'>
                {progressBarDots}
            </div>
        </div>
    )
}

export default Tour
