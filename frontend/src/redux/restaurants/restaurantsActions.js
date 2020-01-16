import {SAVE_RESTAURANT_LIST} from "./restaurantsConstants";

export const saveRestaurantList = restaurantList => {
  return {
    type: SAVE_RESTAURANT_LIST,
    payload: {
      restaurantList
    }
  };
};
