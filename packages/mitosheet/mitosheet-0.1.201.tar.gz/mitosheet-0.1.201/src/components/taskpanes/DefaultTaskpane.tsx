// Copyright (c) Mito
// Distributed under the terms of the Modified BSD License.

import React from 'react';

// import css
import "../../../css/default-taskpane.css"
import XIcon from '../icons/XIcon';
import { TaskpaneInfo, TaskpaneType } from './taskpanes';

/*
    DefaultTaskpane is a higher-order component that
    takes a header and a taskpaneBbody, and displays it as a component.

    The modal has props
    - a header string to be shown at the top of the taskpane
    - a taskpaneBody, a react fragment which is the center segment of the taskpane
    - a setTaskpaneOpenOrClosed function to close the taskpane
*/
const DefaultTaskpane = (
    props: {
        header: string
        taskpaneBody: React.ReactFragment
        setCurrOpenTaskpane: (newTaskpaneInfo: TaskpaneInfo) => void;
    }): JSX.Element => {

    return (
        <div className='default-taskpane-div'>
            <div className='default-taskpane-header-div'>
                <p className='default-taskpane-header-text'>
                    {props.header}
                </p>        
                <div className='default-taskpane-header-exit-button-div' onClick={() => props.setCurrOpenTaskpane({type: TaskpaneType.NONE})}>
                    <XIcon/>
                </div>
            </div>
            <div className='default-taskpane-body-div'> 
                {props.taskpaneBody}
            </div>
        </div>
    )
};

export default DefaultTaskpane;