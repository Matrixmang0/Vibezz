import Vuex from 'vuex';


const store = new Vuex.Store({
    state: {
        message: '',
        selectedParameter: '',
        searchQuery: ''
    },
    mutations: {
      setMessage(state, message) {
        state.message = message;
      },
      resetMessage(state) {
        state.message = '';
      },
      setSelectedParameter(state, parameter) {
        state.selectedParameter = parameter;
      },
      setSearchQuery(state, query) {
        state.searchQuery = query;
      }

    },
    actions: {
      showMessage({ commit }, message) {
        commit('setMessage', message);
        setTimeout(() => {
          commit('resetMessage');
        }, 5000);
      },
      updateSelectedParameter({ commit }, parameter) {
        commit('setSelectedParameter', parameter);
      },
      updateSearchQuery({ commit }, query) {
        commit('setSearchQuery', query);
      }
    }
});

export default store;

