<template>
  <div class="video">
    <button type="button" v-on:click="start()">start</button>
    <button type="button" v-on:click="stop()">stop</button>
    <div ref="videobox"></div>  
  </div>
</template>

<script>
import OT from '@opentok/client';
import axios from 'axios';

export default {
  name: 'OpenTok',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      session_id: null,
      apikey: null,
      token: null,
      id: null,
    }
  },
  methods: {
    start(){
      console.log("start")
      axios.post('https://7287308d.ngrok.io/OpenTok/start_archive/', {'session_id': this.session_id}).then((response => {
        this.id = response.data['archive_id']
      }))
    },
    stop(){
      console.log("stop")
      axios.post('https://7287308d.ngrok.io/OpenTok/stop_archive/', {'archive_id': this.id}).then((response => {
      }))
    }
  },
  mounted(){
    axios.post('https://7287308d.ngrok.io/OpenTok/', {}).then((response => {
      this.apikey = response.data['apikey'];
      this.session_id = response.data['session_id'];
      this.session = OT.initSession(this.apikey, this.session_id);
      this.token = response.data['token'];
      this.session.connect(this.token, (err) => {
        if(err){
          errorHandler(err);
        }
        const publisher = OT.initPublisher(this.$refs.videobox, {width: 1080, height: 720},(response) => {
          this.session.publish(publisher, (response) => {
            console.log("published")
          })
        })
      })
    }))
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
