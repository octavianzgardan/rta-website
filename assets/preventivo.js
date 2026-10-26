// Preventivo automatico — listino ottobre 2026
// Prezzi finali in regime forfettario (nessuna IVA). Oneri pubblici dell'Albo/RENTRI sempre a parte.
var EMAILJS_SERVICE='service_39l9mjp',EMAILJS_TEMPLATE='template_qez2wrs',EMAILJS_KEY='ADqyZw_RXFGZhS5OV';
if(window.emailjs)emailjs.init(EMAILJS_KEY);

var ONORARIO_ISCRIZIONE=390; // prima iscrizione all'Albo, oneri pubblici esclusi
var ans={};

function calcPrice(){
  if(ans.cat==='6')return null;
  var m=parseInt(ans.mezzi)||1,base;
  if(ans.cat==='1'||ans.cat==='4'){
    base = m<=1 ? 220 : (m<=3 ? 290 : 290+40*(m-3));
  }else{ // Cat. 5 oppure 4+5
    base = m<=2 ? 390 : 390+50*(m-2);
  }
  var t=parseInt(ans.tonn)||0;
  if(t>=200000)base*=2;else if(t>=100000)base*=1.7;else if(t>=35000)base*=1.45;else if(t>=10000)base*=1.25;else if(t>=4000)base*=1.1;
  return Math.round(base/5)*5;
}
function eur(n){return '€ '+n.toLocaleString('it-IT')}
function classeLabel(t){
  if(t>=200000)return 'Classe A (oltre 200.000 t/anno)';
  if(t>=100000)return 'Classe B (60.000-200.000 t/anno)';
  if(t>=35000)return 'Classe C (15.000-60.000 t/anno)';
  if(t>=10000)return 'Classe D (6.000-15.000 t/anno)';
  if(t>=4000)return 'Classe E (3.000-6.000 t/anno)';
  return 'Classe F (fino a 3.000 t/anno)';
}
function updateLive(){
  var el=document.getElementById('quiz-live');if(!el)return;
  if(!ans.cat){el.style.display='none';return}
  if(ans.cat==='6'){el.innerHTML='Categoria 6: ti preparo una proposta su misura.';el.style.display='block';return}
  var p=calcPrice();
  el.innerHTML='Stima attuale: <strong>'+eur(p)+'/mese</strong>'+(ans.albo==='no'?' + iscrizione '+eur(ONORARIO_ISCRIZIONE)+' una tantum (oneri pubblici a parte)':'');
  el.style.display='block';
}
function selectOpt(btn,key,val){
  btn.closest('.quiz-options').querySelectorAll('.quiz-opt').forEach(function(b){b.classList.remove('selected')});
  btn.classList.add('selected');ans[key]=val;
  var n=btn.closest('.quiz-step').id.replace('qs','');
  document.getElementById('btn'+n).disabled=false;updateLive();
}
function validateNum(key,val,btnId){
  var n=parseInt(val);
  if(n>0){ans[key]=n;document.getElementById(btnId).disabled=false}else{document.getElementById(btnId).disabled=true}
  updateLive();
}
function checkStep5(){
  var ok=['inp-nome','inp-azienda','inp-email','inp-prov'].every(function(id){return document.getElementById(id).value.trim()});
  document.getElementById('btn5').disabled=!ok;
}
function nextStep(f){document.getElementById('qs'+f).classList.remove('active');document.getElementById('qs'+(f+1)).classList.add('active');document.getElementById('qp'+(f+1)).classList.add('done')}
function prevStep(f){document.getElementById('qs'+f).classList.remove('active');document.getElementById('qs'+(f-1)).classList.add('active')}
function restartQuiz(){
  Object.keys(ans).forEach(function(k){delete ans[k]});
  ['quiz-result','qr-success','qr-error'].forEach(function(id){document.getElementById(id).style.display='none'});
  document.querySelectorAll('.quiz-step').forEach(function(s){s.classList.remove('active')});
  document.getElementById('qs1').classList.add('active');
  document.querySelectorAll('.qp-dot').forEach(function(d,i){d.classList.toggle('done',i===0)});
  document.querySelectorAll('.quiz-opt').forEach(function(b){b.classList.remove('selected')});
  ['inp-mezzi','inp-nome','inp-azienda','inp-email','inp-tel','inp-prov'].forEach(function(id){var e=document.getElementById(id);if(e)e.value=''});
  ['btn1','btn2','btn3','btn4','btn5'].forEach(function(id){document.getElementById(id).disabled=true});
  updateLive();
}
async function sendPreventivo(){
  var g=function(id){return document.getElementById(id).value.trim()};
  var nome=g('inp-nome'),azienda=g('inp-azienda'),email=g('inp-email'),tel=g('inp-tel'),prov=g('inp-prov');
  ans.mezzi=parseInt(document.getElementById('inp-mezzi').value)||1;
  if(!ans.tonn)ans.tonn=500;
  var price=calcPrice();
  var catL={'1':'Categoria 1 (rifiuti urbani)','4':'Categoria 4 (non pericolosi)','5':'Categoria 5 (pericolosi)','45':'Categorie 4 e 5','6':'Categoria 6 (trasporto transfrontaliero)'};
  var alboL={'si':'già iscritto','no':'prima iscrizione'};
  document.getElementById('qs5').classList.remove('active');
  document.getElementById('quiz-result').style.display='block';
  document.getElementById('qr-sending').style.display='block';
  var prezzo;
  if(ans.cat==='6'){prezzo='Categoria 6: proposta personalizzata entro 48 ore lavorative'}
  else{
    prezzo=eur(price)+'/mese, prezzo finale (regime forfettario, nessuna IVA). Pagamento annuale anticipato: '+eur(price*10)+' invece di '+eur(price*12)+' (2 mesi in omaggio).';
    if(ans.albo==='no')prezzo+=' Prima iscrizione all\'Albo: onorario una tantum '+eur(ONORARIO_ISCRIZIONE)+' + oneri pubblici (tassa di concessione governativa, diritti di segreteria, bolli, diritto annuale, RENTRI) che ti indico voce per voce prima di procedere.';
    prezzo+=' Nessun vincolo: disdetta con 60 giorni di preavviso.';
  }
  var params={to_name:nome,to_email:email,azienda:azienda,categoria:catL[ans.cat]||'—',mezzi:ans.mezzi,tonnellate:classeLabel(ans.tonn),prezzo:prezzo,telefono:tel||'non fornito',provincia:prov,albo:alboL[ans.albo]||'—'};
  var done=document.getElementById('qr-done-price');
  if(done)done.textContent=(ans.cat==='6')?'Proposta personalizzata in arrivo':eur(price)+'/mese';
  try{
    await emailjs.send(EMAILJS_SERVICE,EMAILJS_TEMPLATE,params);
    document.getElementById('qr-sending').style.display='none';
    document.getElementById('qr-success').style.display='block';
  }catch(err){
    document.getElementById('qr-sending').style.display='none';
    document.getElementById('qr-error').style.display='block';
    console.error('EmailJS',err);
  }
}
