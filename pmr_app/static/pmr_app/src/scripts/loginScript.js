import '../stylesheets/loginStyles.sass';
import Vue from 'vue'

new Vue({
  el: '#login-app',
  delimiters: ['[[', ']]'],
  data: {
    welcome: '',
    submit: '',
  },
  methods: {
    setContext(pathName) {
      if (pathName == '/login/') {
        this.welcome = 'Welcome back – your rectangles have missed you. Log in here.';
        this.submit = 'Log In';
      } else {
        this.welcome = 'Ready to create some rectangles? Sign up here.';
        this.submit = 'Sign Up';
      }
    },
  },
  beforeMount() {
    this.setContext(window.location.pathname);
  }
});
