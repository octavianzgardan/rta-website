// Menu mobile
(function(){
  var b=document.querySelector('.menu-btn'),n=document.querySelector('nav.main');
  if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)})}
})();

// Vecchi link del sito a pagina unica (#preventivo, ?accetta…) → nuove pagine
(function(){
  if(location.pathname!=='/'&&location.pathname!=='/index.html')return;
  var q=new URLSearchParams(location.search);
  if(q.has('accetta')){location.replace('/attiva/'+location.search);return}
  var map={'#preventivo':'/preventivo/','#servizio':'/preventivo/','#cat6':'/','#raee':'/','#chi-sono':'/chi-sono/','#blog':'/guide/','#obbligo':'/responsabile-tecnico-esterno/','#faq-pubblica':'/#faq'};
  if(map[location.hash]&&map[location.hash]!=='/#faq')location.replace(map[location.hash]);
})();

// Banner cookie (solo informativo: il sito usa cookie tecnici e Google Fonts)
(function(){
  var k='rta-cookie-ok',el=document.getElementById('cookie-banner');
  if(!el)return;
  var seen=null;try{seen=localStorage.getItem(k)}catch(e){}
  if(!seen)setTimeout(function(){el.classList.add('show')},700);
  el.querySelectorAll('button').forEach(function(btn){btn.addEventListener('click',function(){
    try{localStorage.setItem(k,btn.dataset.v||'1')}catch(e){}
    el.classList.remove('show')})});
})();

// Statistiche: conta i clic su WhatsApp ed email (solo se GoatCounter è attivo)
document.addEventListener('click',function(e){
  var a=e.target.closest&&e.target.closest('a[href]');if(!a||!window.goatcounter||!window.goatcounter.count)return;
  var h=a.getAttribute('href'),ev=h.indexOf('wa.me/')>-1?'whatsapp':h.indexOf('mailto:')===0?'email':null;
  if(ev)window.goatcounter.count({path:'clic-'+ev+location.pathname,title:'Clic '+ev,event:true});
});
