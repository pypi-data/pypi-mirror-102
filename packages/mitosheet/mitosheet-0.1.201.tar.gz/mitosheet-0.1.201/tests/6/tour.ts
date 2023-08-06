// Copyright (c) Mito
// Distributed under the terms of the Modified BSD License.

/*
    Contains tests for basic, single sheet mito rendering, column additions,
    and column editing.
*/

import { tryTest } from '../utils/testHelpers';

import { CURRENT_URL } from '../config';
import { doNewPivot } from '../utils/pivotHelpers';
import { tourContinueButton } from '../utils/tourHelpers';

const code = `import pandas as pd

# First, remove the user.json
import os
from pathlib import Path
try:
    os.remove(os.path.join(Path.home(), ".mito", "user.json"))
except:
    pass

import mitosheet
df = pd.DataFrame(data={'A': [1,2,3], 'B': [1,2,3]})
mitosheet.sheet(df)`;

fixture `Test Tour`
    .page(CURRENT_URL)

    
test('Can go through the tour', async t => {
    await tryTest(
        t,
        code, 
        async t => {
            await t.click(tourContinueButton)

            await doNewPivot(t, 'df', ['A'], [], {'A': 'count'})

            await t.click(tourContinueButton)
            await t.click(tourContinueButton)
            await t.click(tourContinueButton)

            // After clicking through the four steps of the tour, the tour should no longer exist
            await t.expect(tourContinueButton.exists).notOk()
        },
        false
    )
});