    

    setInterval(findMyState,1000);
    
    
}
const stopin =() =>{
    let stoptime = setInterval(findMyState,1000);
    clearInterval(stoptime);
}

const findMyState =() =>{
    
    
    console.log('hai');
    const status = document.querySelector('.status');

    const success =(position)=>{
        console.log(position)
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        
        localStorage.setItem('logi',longitude);
        localStorage.setItem('lati',latitude);
        window.location.href = "booking.js";
        
        const geoApiurl = 'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en'

        fetch(geoApiurl)
        .then(res => res.json())
        .then(data =>{
            console.log(data)
        })
    }

    const error =() => {
        status.textContent='Enable';
    }


    navigator.geolocation.getCurrentPosition(success,error);
   
    
}


document.querySelector('.find-state').addEventListener('click',timeintervel);