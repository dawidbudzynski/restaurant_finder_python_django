import {SAVE_SEARCH_PARAMS} from "./searchParamsConstants";

export const saveSearchParams = searchParams => {
  return {
    type: SAVE_SEARCH_PARAMS,
    payload: {
      searchParams
    }
  };
};
