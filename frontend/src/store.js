import Vuex from 'vuex';


const store = new Vuex.Store({
    state: {
        message: '',
    },
    mutations: {
      setMessage(state, message) {
        state.message = message;
      },
      resetMessage(state) {
        state.message = '';
      }
    },
    actions: {
      showMessage({ commit }, message) {
        commit('setMessage', message);
        setTimeout(() => {
          commit('resetMessage');
        }, 5000);
      }
    }
});

export default store;

