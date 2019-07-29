import React from 'react';
import ReactDOM from 'react-dom';

import App from './App';
import './index.scss';

var element = document.createElement('div');

// 通过import导入
element.id = 'app';
document.body.appendChild(element);

let render = () => {
  ReactDOM.render(<App />, element);
};
render();
