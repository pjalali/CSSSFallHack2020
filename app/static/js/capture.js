function startup() {
    console.log("hello")
    const constraints = {
        video: {exact: "environment"},
    };

    const video = document.querySelector('video');

    navigator.mediaDevices.getUserMedia(constraints).then((stream) => {video.srcObject = stream});
}