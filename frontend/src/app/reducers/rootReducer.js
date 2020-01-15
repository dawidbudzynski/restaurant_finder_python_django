import {combineReducers} from "redux";
import {reducer as FormReducer} from 'redux-form';
import saveSearchParams from "../../features/restaurants/eventReducer";

const rootReducer = combineReducers({
  form: FormReducer,
  searchParams: saveSearchParams
});

export default rootReducer;
