import axios from 'axios';

axios.defaults.baseURL = process.env.VUE_APP_ROOT_API;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

export function read(repository) {
  return access(`${repository}/`, 'GET');
}

export function readPage(repository, page = 1) {
  return access(`${repository}/?page=${page}`, 'GET');
}

export function search(repository, word) {
  return access(`${repository}/?q=${word}`, 'GET');
}

export function set(repository, id) {
  return data_access(`${repository}/${id}/`, 'GET');
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

export function fileUpload(repository, params, data={}) {
  return new Promise(resolve => {
    const payload = axios
      .post(`${repository}/`, params, {
        headers: {
          'content-type': 'multipart/form-data',
        },
        data: JSON.stringify(data),
      })
      .then(response => {
        return { payload: response };
      })
      .catch(error => {
        // console.log(error.config);
        return { error };
      });
    resolve(payload);
  });
}

function access(url, method) {
  return new Promise(resolve => {
    const payload = _access(url, {
      method: method,
      headers: {},
    });
    resolve(payload);
  });
}

function data_access(url, method, data) {
  return new Promise(resolve => {
    const payload = _access(url, {
      method: method,
      headers: {
        'content-type': 'application/json',
      },
      data: JSON.stringify(data),
    });
    resolve(payload);
  });
}

function _access(url, config) {
  // console.log("---send---");
  // console.log(config);
  return axios(url, config)
    .then(response => {
      // console.log('response : ', response);
      // console.log(response.data);
      return { payload: response.data };
    })
    .catch(error => {
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        console.log(error.response.data);
        console.log(error.response.status);
        console.log(error.response.headers);
      } else if (error.request) {
        // The request was made but no response was received
        // `error.request` is an instance of XMLHttpRequest in the
        // browser and an instance of
        // http.ClientRequest in node.js
        console.log(error.request);
      } else {
        // Something happened in setting up the request that triggered an Error
        console.log('Error', error.message);
      }
      console.log(error.config);
      return { error };
    });
}
