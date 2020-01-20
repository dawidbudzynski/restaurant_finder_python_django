import {createReducer} from "../../app/common/util/reducerUtils";
import {SAVE_RESTAURANT_LIST} from "./restaurantsConstants";

const initialState = [];

const saveRestaurantList = (state, payload) => {
  return [...state, ...payload.restaurantList];
};

export default createReducer(initialState, {
  [SAVE_RESTAURANT_LIST]: saveRestaurantList
});
