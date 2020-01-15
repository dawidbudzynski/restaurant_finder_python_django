import {SAVE_SEARCH_PARAMS} from "./eventConstants";

export const saveSearchParams = search_params => {
  return {
    type: SAVE_SEARCH_PARAMS,
    payload: {
      search_params
    }
  };
};
