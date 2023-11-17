import * as React from 'react';
import { DataColumn, LensKey } from '../types';
interface Props {
    view: LensKey;
    columns: DataColumn[];
    rowIndex: number;
    syncKey: string;
    deferLoading?: boolean;
}
declare const LensFactory: React.FunctionComponent<Props>;
export default LensFactory;
