## This file provides inventory system.
## アイテムの売買や管理を行う機能を追加するファイルです。
## スキルやクエストなど様々な要素の管理にも汎用的に使えます。

##############################################################################
## How to Use
##############################################################################

## まず最初に、管理するアイテムのタイプのリストを作成します。
define item_types = ["weapon", "supply", "food", "book", "cloth", "various"]

## それから各アイテムを Item(name, type, value, score, max_score, cost, order, prereqs, info) で定義します。
## name は表示される名前、type はカテゴリー、value は価格です。
## score はアイテムを追加時のデフォルトの個数で、省略すると１になります。
## max_score は所持できるアイテムの最大数で、省略またはゼロにすると無限大になります。
## cost を設定すると、アイテム使用時にコスト分の個数が減ります。
## order はデフォルトのソート順を決めたい時に使います。
## prereqs はそのアイテムを購入するときに消費するアイテムです。
## info はマウスフォーカスした時に表示される情報です。
## inventory に与える namespace の名前空間で定義する必要があります。

#Weapons
define item.knife = Item("Knife", type="weapon", value=50, info="knife")
define item.jackknife = Item("Jackknife", type="weapon", value=50, info="Una navaja usada usualmente por delincuentes. Atk +10")
define item.pistol = Item("Pistola 9mm", type="weapon", value=2500, info="Una pistola regular. Atk +100")
define item.excalibur = Item("Excalibur", type="weapon", value=999999, info="La espada legendaria del Rey Arturo. Una espada cuyo poder te permitirá tener una batalla 'ganable', si es que sabes usarla apropiadamente.")
define item.magic = Item("Ultima", type="weapon", value=999999, info="Un hechizo legendario del guerrero Tokaroka. Un poderosísimo hechizo que es, si es que sabes usarla apropiadamente.")
define item.gun = Item("M16 & Grenade launcher", type="weapon", value=999999, info="El rifle legendario de Aldo Mountain (ídolo de [player]). El arma definitiva de un ganster, si es que sabes usarla apropiadamente.")
#Supply
define item.pillatk = Item("+Atk Pills", type="supply", value=250, info="Multiplica tu Ataque en combate x2.")
define item.pilldef = Item("+Def Pills", type="supply", value=250, info="Multiplica tu Defensa en combate x2.")
define item.pillspd = Item("+Spd Pills", type="supply", value=250, info="Multiplica tu Velocidad en combate x2.")
define item.pillmat = Item("+MAt Pills", type="supply", value=250, info="Multiplica tu At. Mágico en combate x2.")
define item.pillmdf = Item("+MDf Pills", type="supply", value=250, info="Multiplica tu Df. Mágica en combate x2.")
#Food
define item.apple = Item("Apple", type="food", value=10, info="Una manzana roja apetitosa. Restaura 75 HP.")
define item.orange = Item("Orange", type="food", value=20, info="Una naranja jugosa y dulce. Restaura 50 HP y 50 MP.")
define item.juice = Item("Juice", type="food", value=30, prereqs="orange:1, apple:2", info="Jugo multifruta. Requiere 2 manzana y 1 naranja. Restaura 150 HP y 100 MP.")
define item.cmonbun = Item("Cinnamon Bun", type="food", value=5000, info="Un rol de canela tan dulce cómo Sayori. Restaura tus HP y MP al máximo, neutraliza la redución de Stats, cura cualquier estado alterado.")
define item.yuritea = Item("Oolong tea", type="food", value=5000, info="Un té preparado por Yuri con mucho amor. Restaura tus HP y MP al máximo, neutraliza la redución de Stats, cura cualquier estado alterado.")
define item.natcake = Item("Natsuki's cupcake", type="food", value=5000, info="Los típicos y tiernos cupcakes de Natsuki. Restaura tus HP y MP al máximo, neutraliza la redución de Stats, cura cualquier estado alterado.")
define item.monicoffee = Item("Tarbrush coffee", type="food", value=5000, info="Un café que le gusta presumir Monika en sus redes sociales. Restaura tus HP y MP al máximo, neutraliza la redución de Stats, cura cualquier estado alterado.")
define item.cookie = Item("Cookie", type="food", value=10, info="Una galleta dulce y rica. Restaura 100 HP.")
define item.proteinbar = Item("Protein bar", type="food", value=80, info="Una barra de proteinas, que en realidad es sólo un snack. Restaura 100 HP.")
define item.cupcake = Item("Cupcake", type="food", value=10, info="Un cupcake regular. Restaura 100 HP.")
define item.sportdrink = Item("Sport drink", type="food", value=10, info="Una bebida energética que te ayuda a hidratarte. Restaura 100 HP.")
define item.chocolate = Item("Chocolate", type="food", value=10, info="Una barra de chocolate rico para compartir con quienes amas. Restaura 100 HP.")
define item.soda = Item("Soda", type="food", value=10, info="Una gaseosa. Restaura 100 HP.")
define item.schoollunch = Item("Almuerzo escolar", type="food", value=10, info="Un almuerzo de la escuela. No es muy rico que digamos...")
#Books
define item.sbook1 = Item("Happy Thoughts book", type="book", value=650, info="Un libro que te ayudará a escribir poemas para Sayori.")
define item.ybook1 = Item("Dark in the blossoms book", type="book", value=650, info="Un libro que te ayudará a escribir poemas para Yuri.")
define item.nbook1 = Item("Anime & stuff book", type="book", value=650, info="Un libro que te ayudará a escribir poemas para Natsuki.")
define item.mbook1 = Item("Shadows of epiphany", type="book", value=500, info="Un libro que te ayudará a escribir poemas para Monika.")
define item.mcbook1 = Item("Car Thief 5 - The Guide", type="book", value=300, info="Un libro con información sobre el juego Ladrón de Autos 5.")
define item.mcbook2 = Item("Pet Monsters Hawaii - The Guide", type="book", value=500, info="Un libro con información sobre el juego Monstruomascotas Hawaii.")
define item.mcbook3 = Item("Symbol of Blaze: Destiny - The Guide", type="book", value=400, info="Un libro con información sobre el juego Símbolo de llamas: Destino.")
define item.mcbook4 = Item("Otaku Ninja Ultimate 4 - The Guide", type="book", value=250, info="Un libro con información sobre el juego El ninja otaku Ultimate 4.")
define item.mcbook5 = Item("Life Simulator 5 - The Guide", type="book", value=600, info="Un libro con información sobre el juego Simulador de vida 5.")
#Clothes
define item.cloth = Item("[player]'s casual clothes", type="outfit", value=0, info="Una camiseta negra, jeans azules y zapatos baratos.")
define item.cloth = Item("School Uniform", type="outfit", value=0, info="Uniforme escolar de [player].")
define item.cloth = Item("School Dress", type="outfit", value=0, info="Uniforme femenino de la escuela ¿Qué carajos haces con eso?")
#Various
define item.mcvideogame = Item("Car Thief 5", type="various", value=6000, info="Ladrón de Autos 5. El juego que [player] ansiaba mucho jugar.")
define item.svideogame = Item("Pet Monsters Hawaii", type="various", value=5000, info="Monstruomascotas Hawaii. Un juego interesante para Sayori.")
define item.yvideogame = Item("Symbol of Blaze: Destiny", type="various", value=4000, info="Símbolo de llamas: Destino. Un juego interesante para Yuri.")
define item.nvideogame = Item("Otaku Ninja Ultimate 4", type="various", value=5000, info="El ninja otaku Ultimate 4. Un juego interesante para Natsuki.")
define item.mvideogame = Item("Life Simulator 5", type="various", value=7000, info="Simulador de vida 5. Un juego interesante para Monika (Si es que le interesa los videojuegos).")


## 最後にアイテムの管理者を Inventory(money, item_types, namespace, tradein, infinite, recharge, removable, items) で定義します。
## money は所持金です。
## item_types は上で定義したアイテムタイプのリストで、アイテム画面でのカテゴリー分けに使用します。
## カテゴリーに合わないタイプのアイテムも入手可能ですが、画面には表示されません。
## namespace を設定すると、その管理者が扱うアイテムを名前空間ごとに分けることが出来ます。
## tradein はその所持者が下取りする時の価格比です。
## infinite を True にすると所持金が無限になります。
## recharge を True にすると、常に在庫が補充されます。
## removable を False にすると、在庫がゼロになってもアイテム覧から消去されません。
## items を設定すると下で説明する add_items と同じ効果があります。

default house_inventory = Inventory(item_types = item_types, namespace = "item")
default bag_inventory = Inventory(item_types = item_types, namespace = "item")
default merchant = Inventory(item_types = item_types, namespace = "item", tradein=.25, infinite=True, recharge=True, removable=False)


## ゲームがスタートしたら jump sample_inventory でここに飛んでください。

label sample_inventory:

    ## add_item(item, score) でアイテムを追加します。個数を指定する場合は引数 score を使います。
    ## item は item. を外した文字列です。
    #$ house_inventory.add_item("apple", score=2)

    ## add_all_items(types, charge=True) で名前空間で定義したすべてのアイテムのうち、タイプが合致するものを自動的に追加します。
    ## charge が True の場合、max_score まで追加されます。
    $ merchant.add_all_items()

    ## 他に以下のメソッドがあります。
    ## has_item(item) - 所持していれば True を返します。
    ## count_item(item) - 所持している合計の個数を返します。
    ## charge_item(item, score) - 所持しているアイテムを最大数までチャージします。スコアを与えるとスコア分チャージします。
    ## charge_all_items(types, score) - 所持している types に含まれるアイテムを最大数またはスコア分までチャージします。
    ## add_items(items, score) - "a,b,c" のように複数のアイテム名与えると、その全てのアイテムを追加できます。
    ## remove_item(item) - 所持していればそのアイテムを消去します。
    ## remove_items(items) - "a,b,c" のように複数のアイテム名与えると、所持していればそのアイテムを消去します。
    ## score_item(item, score) - アイテムの個数を変更して、１以上なら獲得、０以下なら消去します。
    ## score_items(item, score) - "a,b,c" のように複数のアイテム名与えると、複数の個数を変更・獲得・消去します。
    ## give_item(item, getter, score) - アイテムを getter に渡します。
    ## can_buy_item(item, score) - アイテムが購入可能かどうか調べます。
    ## buy_item(item, score) - 所持金と要求アイテムが足りていれば、それを消費してアイテムを追加します。
    ## sell_item(item, buyer, score) - アイテムを buyer に売却し、所持金を受け取ります。
    ## can_use_item(item, target, cost="cost") - アイテムが使用可能かどうか調べます。cost="money" にすると money を消費します。
    ## use_item(item, target, cost="cost") - アイテムを target に使用します。効果は各アイテムごと定義してください。

    ## 次のメソッドは内部使用です。
    ## get_item(name) - 文字列の name から Item オブジェクトを取得します。
    ## get_items(types, score) - score 以上で types に含まれるアイテムのリストを (name, score, obj) のタプルで返します。
    ## sort_items(order="order") - アイテムをソートします。


    while True:

        ## 次の命令はロールバックをブロックして、ゲームの全ての変化をセーブできるようにします。
        ## （デフォルトでは現在の入力待ちの開始時点のみをセーブするので必要になります。）
        $ block()

        menu:

            ## call screen inventory(inv, buyer, title) でアイテムの一覧を表示します。

            "Show inventory":
                ## アイテムを見たり整理したい時は inventory(表示する所持者) を使います。
                ## この状態でアイテムをクリックすると、スロットの入替えモードになります。
                $ block()
                call screen inventory(bag_inventory)

            "House trunk":
                ## アイテムを見たり整理したい時は inventory(表示する所持者) を使います。
                ## この状態でアイテムをクリックすると、スロットの入替えモードになります。
                $ block()
                call screen inventory(house_inventory)

            "return":
                return
                #$ renpy.full_restart()

##############################
########## Market ############
##############################
label market_inventory:

    $ merchant.add_all_items()

    while True:

        ## 次の命令はロールバックをブロックして、ゲームの全ての変化をセーブできるようにします。
        ## （デフォルトでは現在の入力待ちの開始時点のみをセーブするので必要になります。）
        $ block()

        menu:

            ## call screen inventory(inv, buyer, title) でアイテムの一覧を表示します。

            "Show inventory":
                ## アイテムを見たり整理したい時は inventory(表示する所持者) を使います。
                ## この状態でアイテムをクリックすると、スロットの入替えモードになります。
                $ block()
                call screen inventory(bag_inventory)

            "Buy items":
                ## アイテム買いたい時は inventory(売り手の所持者、買い手の所持者) を使います。
                $ block()
                call screen inventory(merchant, buyer=bag_inventory, title="Buy")

            "Sell items":
                ## アイテム売りたい時も inventory(売り手の所持者、買い手の所持者) を使います。
                ## 売買の相手が逆転するだけですが、スクリーンタイトルを変えています。
                $ block()
                call screen inventory(bag_inventory, buyer=merchant, title="Sell")

            "return":
                return
                #$ renpy.full_restart()


##############################################################################
## Definitions
##############################################################################

init python:

    def block():
        # blocks rollback then allows saving data in the current interaction

        config.skipping = None
        renpy.checkpoint()
        renpy.block_rollback()
        renpy.retain_after_load()


##############################################################################
## Inventory Screen

## screen that shows inventory
## inv is an inventory object that has items on the screen
## if buyer is given, it's trade mode.
## otherwise, it's stock mode that can reorder item slots

screen inventory(inv, buyer=None, title="Inventory"):

    # screen variables
    default tab = "all"

    if title=="Buy":
        default confirm_message = "Are you sure to buy it?"
    else:
        default confirm_message = "Are you sure to sell it?"

    default notify_message = "You don't have money or required items"

    # frame size
    python:
        width = config.screen_width*3//4
        height = config.screen_height//2

    # unselect item on show
    on "show" action SetField(inv, "selected", None)

    vbox:
        # screen title
        label title text_size gui.title_text_size

        # money. when seller (inv) is an infinite inventory, show buyer's money
        $ money = inv.money if not inv.infinite else buyer.money
        #text "money:[money:>5]" xalign .5

        null height 60

        # sort buttons
        text "Sort by"
        for i in ["name", "type", "value", "amount", "order"]:
            textbutton i.capitalize():
                action Function(inv.sort_items, order=i)

    vbox align .5,.6:

        # category tabs
        hbox style_prefix "radio":

            for i in ["all"] + inv.item_types:
                textbutton i.capitalize():
                    action SetScreenVariable("tab", i)

        # item slots
        frame xysize width, height:

            vpgrid style_prefix "item":
                cols 3 mousewheel True draggable True scrollbars "vertical"

                for name, score, obj in inv.get_items(types=[tab] if tab != "all" else inv.item_types):

                    $ price = int(obj.value*(buyer.tradein if buyer else inv.tradein))

                    textbutton "[obj.name] x[score]":
                        selected inv.selected == name
                        tooltip obj.info

                        # Sell/buy mode
                        if buyer:
                            if buyer.can_buy_item(name):
                                action Confirm(confirm_message, Function(inv.sell_item, name=name, buyer=buyer))
                            else:
                                action Notify(notify_message)

                        # Arrange mode
                        else:

                            # reorder after selected
                            if inv.selected:
                                action [Function(inv.replace_items, first=name, second=inv.selected),
                                        SetField(inv, "selected", None)]

                            # reorder before selecting
                            else:
                                action SetField(inv, "selected", name)

                            # This action uses item.
                            # action Function(inv.use_item, name=name, target=?)

        null height 10

        # information window
        frame xysize width, height//3:
            $ tooltip = GetTooltip() or ""
            text [tooltip]

    textbutton "Return" action Return() yalign 1.0

    key "game_menu" action [SetField(inv, "selected", None) if inv.selected else Return()]


style item_button:
    xsize 300
    ysize 75


##############################################################################
## Inventory class.

init -10 python:

    from collections import OrderedDict

    class Inventory(object):

        """
        Class that stores items. It has following fields:
        money - score of money this object has.
        item_types - list of item type that are grouped up as tab in the inventory screen.
        namespace - if given, items defined in this name space are used
        tradein - when someone buyoff items to this inventory, value is reduced by this value
        infinite - if True, money is infinite.
        recharge - if True, an item score is charged at max_score (or 1) when its score is changed
        removable = if False, an item is not removed when score reached at 0.
        items - ordered dictionary of {"item name": score}.
            if items property given at the init time, they are added by add_items method,
        selected - selected slot in a current screen.
        """


        def __init__(self, money = 0, item_types= None, namespace=None, tradein = 1.0, infinite = False, recharge=False, removable = True, items=None):

            self.money = int(money)
            self.item_types = item_types or []
            self.namespace = getattr(store, namespace) if namespace else store
            self.tradein = float(tradein)
            self.infinite = infinite
            self.recharge = recharge
            self.removable = removable
            self.items = OrderedDict()
            if items:
                self.add_items(items)
            self.selected = None


        def get_item(self, name):
            # returns item object from name

            if isinstance(name, Item):
                return name

            elif isinstance(name, basestring):
                obj = getattr(self.namespace, name, None)
                if obj:
                    return obj

            raise Exception("Item '{}' is not defined".format(name))


        def get_items(self, types = None, score=None, rv=None):
            # returns list of (name, score, object) tuple in conditions
            # if rv is "name" or "obj", it returns them.

            items = [k for k, v in self.items.items() if score==None or v >= score]

            types = types or self.item_types
            items = [i for i in items if self.get_item(i).type in types]

            if rv == "name":
                return items

            elif rv == "obj":
                return [self.get_item(i) for i in items]

            return  [(i, self.items[i], self.get_item(i)) for i in items]


        def has_item(self, name, score=None):
            # returns True if inventory has this item whose score is higher than given.

            # check valid name or not
            self.get_item(name)

            return name in [k for k, v in self.items.items() if score==None or v >= score]


        def has_items(self, name, score=None):
            # returns True if inventory has these items whose score is higher than give.
            # "a, b, c" means a and b and c, "a | b | c" means a or b or c.

            separator = "|" if name.count("|") else ","
            names = name.split(separator)
            for i in names:
                i = i.strip()
                if separator == "|" and self.has_item(i, score):
                    return True
                elif separator == "," and not self.has_item(i, score):
                    return False

            return True if separator == ","  else False


        def count_item(self, name):
            # returns score of this item

            if self.has_item(name):
                return self.items[name]


        def charge_item(self, name, score=None):
            # changes score of name to its maximum value

            if self.has_item(name):
                if score:
                    self.items[name] += score
                else:
                    self.items[name] = max(self.get_item(name).max_score, 1)


        def charge_all_items(self, types=None):
            # charges all items in self.items.

            types = types or self.item_types

            for i in self.items.keys():
                if self.get_item(i).type in types:
                    self.charge_item(i)


        def add_item(self, name, score = None):
            # add an item
            # if score is given, this score is used instead of item's default value.

            score = score or self.get_item(name).score
            max_score = self.get_item(name).max_score

            if self.has_item(name):
                self.items[name] += score
            else:
                self.items[name] = score

            if max_score > 0:
                self.items[name] = min(self.items[name], max_score)

            if self.recharge:
                self.charge_item(name)


        def add_items(self, items, score=None):
            # add items

            for i in items.split(","):
                i = i.strip()
                score = score or self.get_item(i).score
                self.add_item(i, score=score)


        def add_all_items(self, types=None, charge=True, sort="order"):
            # get all Item objects defined under namespace

            types = types or self.item_types

            for i in dir(self.namespace):
                if isinstance(getattr(self.namespace, i), Item):
                    if self.get_item(i).type in types:
                        self.add_item(i)
                        if charge:
                            self.charge_item(i)

            self.sort_items(order=sort)


        def remove_item(self, name):
            # remove an item

            if self.has_item(name):
                del self.items[name]


        def remove_items(self, items):
            # remove items

            for i in items.split(","):
                i = i.strip()
                self.remove_item(i)


        def score_item(self, name, score):
            # changes score of name

            self.add_item(name, score)
            if self.removable and self.items[name] <= 0:
                self.remove_item(name)


        def score_items(self, name, score):
            # changes score of name

            for i in items.split(","):
                self.add_item(name, score)
                if self.removable and self.items[name] <= 0:
                    self.remove_item(name)


        def give_item(self, name, getter, score=None):
            # remove an item slot then add this name to getter

            score = score or self.get_item(name).score

            if self.has_item(name, score):

                getter.score_item(name, score)
                self.score_item(name, -score)


        def can_buy_item(self, name, score = None, prereqs=True):
            # returns True if this item can be bought

            score = score or self.get_item(name).score
            value = self.get_item(name).value*score
            prereqs = self.get_item(name).prereqs

            if self.infinite:
                return True

            if self.money < value:
                return False

            if prereqs:
                for k,v in prereqs.items():
                    if not self.has_item(k, score=v*score):
                        return False

            return True


        def buy_item(self, name, score = None, prereqs=True):
            # buy an item
            # if prereqs is True, it requires items listed in prereqs

            if not self.can_buy_item(name, score, prereqs):
                return False

            score = score or self.get_item(name).score
            value = self.get_item(name).value*score
            prereqs = self.get_item(name).prereqs

            self.add_item(name, score)
            if not self.infinite:
                self.money -= value

            if prereqs:
                for k,v in prereqs.items():
                    self.score_item(k, score=-v*score)


        def sell_item(self, name, buyer, score = None, prereqs=True):
            # remove an item then add this item to buyer for money

            if self.has_item(name):

                score = score or self.get_item(name).score
                value = self.get_item(name).value*score

                buyer.buy_item(name, score, prereqs)

                if buyer.infinite or buyer.money >= value:
                    self.score_item(name, score=-score)
                    if not self.infinite:
                        self.money += int(value*buyer.tradein)


        def replace_items(self, first, second):
            # swap order of two slots

            keys = list(self.items.keys())
            values = list(self.items.values())
            i1 = keys.index(first)
            i2 = keys.index(second)
            keys[i1], keys[i2] = keys[i2], keys[i1]
            values[i1], values[i2] = values[i2], values[i1]

            self.items = OrderedDict(zip(keys, values))


        def sort_items(self, order="order"):
            # sort slots

            items = self.items.items()

            if order == "name":
                items.sort(key = lambda i: self.get_item(i[0]).name)
            elif order == "type":
                items.sort(key = lambda i: self.item_types.index(self.get_item(i[0]).type))
            elif order == "value":
                items.sort(key = lambda i: self.get_item(i[0]).value, reverse=True)
            elif order == "amount":
                items.sort(key = lambda i: i[1], reverse=True)
            elif order == "order":
                items.sort(key = lambda i: self.get_item(i[0]).order)

            self.items = OrderedDict(items)


        def can_use_item(self, name, target=None, cost="cost"):
            # returns True if inv can use this item

            obj = self.get_item(name)

            if cost=="cost" and self.count_item(name) >= obj.cost:
                return True
            elif cost=="value" and (self.money >= obj.value or self.infinite):
                return True
            return False


        def use_item(self, name, target=None, cost="cost"):
            # uses item on target

            if not self.can_use_item(name, target, cost):
                return False

            obj = self.get_item(name)

            if cost=="cost" and obj.cost:
                self.score_item(name, -obj.cost)

            elif cost=="value" and obj.value and not self.infinite:
                self.money -= value


            ## write script here



##############################################################################
## Item class.

    class Item(object):

        """
        Class that represents item that is stored by inventory object. It has following fields:
        name - item name that is shown on the screen
        type - item category
        value - price that is used for trading
        score - default amount of item when it's added into inventory
        max_score - maximum score. Score higher than this is ignored. 0 is infinite.
        cost - if not zero, using this item reduces score.
        order - if integer is given, item can be sorted by this number.
        prereqs - required items to buy. This should be given in strings like "itemA:1, itemB:2"
        info - description that is shown when an item is focused
        """


        def __init__(self, name="", type="", value=0, score=1, max_score = 0, cost=0, order=0, prereqs=None, info="", **kwargs):

            self.name = name
            self.type = type
            self.value = int(value)
            self.score = int(score)
            self.max_score = int(max_score)
            self.cost = int(cost)
            self.order = int(order)

            self.prereqs = {}
            if prereqs:
                for i in [x.split(":") for x in prereqs.split(",")]:
                    self.prereqs.setdefault(i[0].strip(), int(i[1]))
            self.info = info

            for i in kwargs.keys():
                setattr(self, i, kwargs[i])

