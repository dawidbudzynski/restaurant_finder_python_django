import {createReducer} from "../../app/common/util/reducerUtils";
import {SAVE_SEARCH_PARAMS} from "./searchParamsConstants";

const initialState = [];

const saveSearchParams = (state, payload) => {
  return [...state, payload.searchParams];
};

export default createReducer(initialState, {
  [SAVE_SEARCH_PARAMS]: saveSearchParams,
});
