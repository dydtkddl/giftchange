let input1 = document.querySelector('#input1');
                let input2 = document.querySelector('#input2');
                let input3 = document.querySelector('#input3');
                let input4 = document.querySelector('#brand1');
                input1.addEventListener('input', (e)=> {
                    value1 = e.target.value;
                    input2.addEventListener('input', (e)=>{
                        value2 = e.target.value;
                        input3.addEventListener('input', (e)=>{
                            value3=e.target.value;
                            input4.addEventListener('change',(e)=>{
                                value4 = e.target.value;
                            let code =`<a href='/app/second/?${value1}?${value2}?${value3}?${value4}'>입력다했으면 클릭<a>`;
                                document.querySelector('#div').innerHTML = code;
                            })
                        })
                    })
                })