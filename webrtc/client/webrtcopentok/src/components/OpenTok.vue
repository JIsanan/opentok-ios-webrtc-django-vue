<template>
  <div class="video">
    <button type="button" v-if="isallowed & !archiving" v-on:click="start()">start</button>
    <button type="button" v-if="archiving" v-on:click="stop()">stop</button>
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
      server: 'INSERT YOUR SERVER URL HERE',
      session_id: null,
      apikey: null,
      token: null,
      id: null,
      isallowed: null,
      archiving: false,
    }
  },
  methods: {
    start(){
      console.log("start")
      axios.post(this.server+'OpenTok/start_archive/', {'session_id': this.session_id}).then((response => {
        this.id = response.data['archive_id']
        this.archiving = true
      }))
    },
    stop(){
      console.log("stop")
      axios.post(this.server+'OpenTok/stop_archive/', {'archive_id': this.id}).then((response => {
        this.archiving = false
      }))
    }
  },
  mounted(){
    axios.post(this.server+'OpenTok/', {}).then((response => {
      this.apikey = response.data['apikey'];
      this.session_id = response.data['session_id'];
      this.session = OT.initSession(this.apikey, this.session_id);
      this.token = response.data['token'];
      this.session.connect(this.token, (err) => {
        if(err){
          errorHandler(err);
        }
        const publisher = OT.initPublisher('publsher', this.$refs.videobox, {width: 640, height: 480},(response) => {
          this.session.publish(publisher, (response) => {
            console.log("published")
            this.isallowed = true
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
