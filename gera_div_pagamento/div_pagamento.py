def main(param):
    return{'pagamento': """<div class="column column3">
             <div class="step" id="step5">
                <div class="number">
                    <span>4</span>
                </div>
                <div class="title">
                    <h1>Finalizar Pagamento</h1>
                </div>
                <div class="modify">
                    <i class="fa fa-plus-circle"></i>
                </div>
             </div>
             <div class="content" id="final_products">
                <div class="left" id="ordered">
                    <div class="products">
                        <div class="product_image">
                            <img src="https://i.imgur.com/zj4hrKm.jpeg"/>
                        </div>
                        <div class="product_details">
                            <span class="product_name">Computador Vintage</span>
                            <span class="quantity">1 </span>
                            <span class="price">R$450,00</span>
                        </div>
                    </div>
                    <div class="totals">
                        <span class="subtitle">Subtotal <span id="sub_price">R$450,00</span></span>
                        <span class="subtitle">Taxas <span id="sub_tax">R$50,00</span></span>
                        <span class="subtitle">Frete <span id="sub_ship">R$10,00</span></span>
                    </div>
                    <div class="final">
                        <span class="title">Total <span id="calculated_total">R$510.00</span></span>
                    </div>
                </div>	
                <div class="right" id="reviewed">
                    
                    
                    <div id="complete2">
                    <a class="big_button" type='button' onsubmit="return false" id="complete"  href= "" onclick="runScript();" >Finalizar Compra</a>                    
                    
                </div>
                 
            </div>"""
        }
