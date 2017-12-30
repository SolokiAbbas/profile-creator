import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';


const middlewares = [thunk];

const configureStore = (preloadedState = {}) => (
  createStore(
    preloadedState,
    applyMiddleware(...middlewares)
  )
);

export default configureStore;
