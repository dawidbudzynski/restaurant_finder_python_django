import {combineReducers} from "redux";
import {reducer as FormReducer} from 'redux-form';
import searchParamsReducer from "../../redux/searchParams/searchParamsReducer";
import restaurantsReducer from "../../redux/restaurants/restaurantsReducer";

const rootReducer = combineReducers({
  form: FormReducer,
  searchParams: searchParamsReducer,
  restaurants: restaurantsReducer
});

export default rootReducer;
