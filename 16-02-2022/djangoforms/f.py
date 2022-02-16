
        item=Item.objects.filter(item_id=id).first()
        context['item']=item
        context['id']=item.item_id
        
        if id:
            
            item1=Item.objects.filter(item_id=item_id).first()
            item1.name=name
            item1.price=price
            item1.img=img
            item1.discription=discription
            item1.save()
            
            return redirect("home")