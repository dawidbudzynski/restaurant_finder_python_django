import {SEARCH_RESTAURANTS} from "./eventConstants";

export const searchRestaurants = restaurant => {
  return {
    type: SEARCH_RESTAURANTS,
    payload: {
      restaurant
    }
  };
};
