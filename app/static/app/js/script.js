var paypal = document.querySelector('#paypal');
var transferencia = document.querySelector('#transferencia');


document.querySelector('#div_paypal').style.display = 'none';

paypal.addEventListener('click', changePaypal);

function changePaypal(event)
{
      var divpay =   document.querySelector('#div_paypal').style.display = 'block';
      if (divpay != 'block')
      {
             document.querySelector('#div_paypal').style.display = 'none';

      }
  
}