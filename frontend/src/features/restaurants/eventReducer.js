import {createReducer} from "../../app/common/util/reducerUtils";
import {SEARCH_RESTAURANTS} from "./eventConstants";

const initialState = [];

const searchRestaurants = (state, payload) => {
  return [...state, payload.restaurant];
};

export default createReducer(initialState, {
  [SEARCH_RESTAURANTS]: searchRestaurants
});
