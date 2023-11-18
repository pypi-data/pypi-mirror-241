/// <reference types="react" />
import { LensSettings, Setter } from '../types';
interface LensContextType {
    settings: LensSettings;
    onChangeSettings: Setter<LensSettings>;
}
declare const LensContext: import("react").Context<LensContextType>;
export default LensContext;
