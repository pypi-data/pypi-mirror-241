import * as React from 'react';
import { DataColumn, LensKey, LensSettings, Setter } from '../types';
interface Props {
    view: LensKey;
    columns: DataColumn[];
    rowIndex: number;
    syncKey: string;
    deferLoading?: boolean;
    settings: LensSettings;
    onChangeSettings: Setter<LensSettings>;
}
declare const LensFactory: React.FunctionComponent<Props>;
export default LensFactory;
