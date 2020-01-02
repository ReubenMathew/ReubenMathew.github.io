<template>
  <div>
    <p>Home page</p>
    <p>Currently Listening To: {{ track }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
	data () {
	    return {
	    	track: ''
	    }
  	}, methods: {
		getTrack() {
			this.track = this.getTrackFromBackend()
		},
		getTrackFromBackend() {
		    const path = `http://localhost:5000/api/spotify`
		    axios.get(path)
		    .then(response => {
		    	this.track = response.data.curr
		    })
		    .catch(error => {
		    	console.log(error)
		    })
	  	}
	}, created () {
	    this.getTrack(),
	    this.getTrackFromBackend()
  }
}

</script>