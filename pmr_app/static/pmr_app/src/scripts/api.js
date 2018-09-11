import axios from 'axios';

export default {
  getUserGallery(userID) {
    return axios.get('/api/' + userID + '/gallery/');
  },
  createRectangle(userID, width, height, border, color) {
    return axios.post('/api/create_rectangle/', {
      width: width,
      height: height,
      border_radius: border,
      background_color: color,
      user: userID,
    });
  },
  deleteRectangle(rectangle_id) {
    return axios.get('/api/delete_rectangle/' + rectangle_id + '/');
  },
};
