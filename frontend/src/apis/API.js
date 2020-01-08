import axios from 'axios';
import store from '../store';

axios.defaults.baseURL = process.env.VUE_APP_ROOT_API;

function setAuthHeader() {
  const token = localStorage.getItem('token');
  if (token !== null) {
    store
      .dispatch('auth/update')
      .then(() => {
        axios.defaults.headers.common['Authorization'] = 'JWT ' + token;
      })
      .catch(error => {
        if (error.response.status === 401) {
          store.dispatch('auth/logout').then(() => {
            setAuthHeader();
          });
        }
      });
  } else {
    axios.defaults.headers.common['Authorization'] = '';
  }
}

export function read(repository) {
  return access(`${repository}/`, 'GET');
}

export function readPage(repository, page = 1) {
  return access(`${repository}/?page=${page}`, 'GET');
}

export function searchGeo(
  repository,
  name = '',
  address = '',
  prefecture = '',
  river = '',
  waterSystem = '',
  page = ''
) {
  return access(
    `${repository}/?name=${name}&address=${address}&prefecture=${prefecture}&river=${river}&water_system=${waterSystem}&page=${page}`,
    'GET'
  );
}

export function setQuery(repository, query, id) {
  return access(`${repository}/?${query}=${id}`, 'GET');
}

export function create(repository, data) {
  return data_access(`${repository}/`, 'POST', data);
}

export function update(repository, id, data) {
  return data_access(`${repository}/${id}/`, 'PATCH', data);
}

export function destroy(repository, id) {
  return access(`${repository}/${id}/`, 'DELETE');
}

export function fetchUrl(url) {
  return access(url, 'GET');
}

export function fileUpload(repository, params) {
  return new Promise((resolve, reject) => {
    axios
      .post(`${repository}/`, params, {
        headers: {
          'content-type': 'multipart/form-data',
        },
      })
      .then(response => {
        resolve({ payload: response });
      })
      .catch(error => {
        reject(error);
      });
  });
}

function access(url, method) {
  return _access(url, {
    method: method,
    headers: {},
  });
}

function data_access(url, method, data) {
  return _access(url, {
    method: method,
    headers: {
      'content-type': 'application/json',
    },
    data: JSON.stringify(data),
  });
}

function _access(url, config) {
  setAuthHeader();
  return new Promise((resolve, reject) => {
    axios(url, config)
      .then(response => {
        resolve({ payload: response.data });
      })
      .catch(error => {
        // if (error.response) {
        // console.log(error.response.data);
        // console.log(error.response.status);
        // console.log(error.response.headers);
        // } else if (error.request) {
        // The request was made but no response was received
        // console.log(error.request);
        // } else {
        // console.log('Error', error.message);
        // }
        // console.log(error.config);
        reject(error);
      });
  });
}
