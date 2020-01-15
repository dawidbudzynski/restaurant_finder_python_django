import {createReducer} from "../../app/common/util/reducerUtils";
import {SAVE_SEARCH_PARAMS} from "./eventConstants";

const initialState = [];

const saveSearchParams = (state, payload) => {
  return [...state, payload.search_params];
};

export default createReducer(initialState, {
  [SAVE_SEARCH_PARAMS]: saveSearchParams
});
