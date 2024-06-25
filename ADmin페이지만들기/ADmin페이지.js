function setDisplayAppreance(self){
    var body = document.querySelector('body'); 
    var btn = document.getElementById('btnDisplayMode'); 
    if(self.value === '다크모드'){  
      body.style.backgroundColor = 'black';
      body.style.color = 'white'; 
      btn.style.backgroundColor = "yellow"; 
      btn.style.color = "black"; 
      self.value = '라이트모드';
    }else {
      body.style.backgroundColor = 'white';
      body.style.color = 'black';
      btn.style.backgroundColor = "black";
      btn.style.color = "white";
      self.value = '다크모드';
    }
  }

  
  const currentDate = new Date();


  const year = currentDate.getFullYear();
  const month = currentDate.getMonth() + 1;
  const day = currentDate.getDate();
  const hours = currentDate.getHours();
  const minutes = currentDate.getMinutes();
  const seconds = currentDate.getSeconds();


  const formattedDate = `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')} ${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;


  document.write(formattedDate);