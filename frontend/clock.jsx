import React from 'react';
import ReactDOM from 'react-dom';
import configureStore from './store';
import Root from './root';

document.addEventListener('DOMContentLoaded', () => {
  let store = configureStore();
  window.store = store;
  window.dispatch = store.dispatch;
  window.getState = store.dispatch;
  const root = document.getElementById('root');
  ReactDOM.render(<Root store={store}/>, root);
});
