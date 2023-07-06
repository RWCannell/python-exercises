export class Item {
    name: string;
    sellIn: number;
    quality: number;

    constructor(name: string, sellIn: number, quality: number) {
        this.name = name;
        this.sellIn = sellIn;
        this.quality = quality;
    }
}

export class GildedRose {
    items: Array<Item>;

    constructor(items = [] as Array<Item>) {
        this.items = items;
    }

    // this function is called for 'Aged Brie' and 'Backstage Passes'
    updateQualityForSpecialCases(item: Item, qualityFactor: number): void {
        if (item.sellIn <= 10 && item.sellIn > 5) {
            item.quality = item.quality + 2 * qualityFactor;
        }
        if (item.sellIn <= 5) {
            item.quality = item.quality + 3 * qualityFactor;
        }
        if (item.sellIn == 0) {
            item.quality = 0;
        }
        item.sellIn = item.sellIn - 1;
    }

    updateQualityForConjured(item: Item, qualityFactor: number): void {
        // quality decreases twice as fast as normal items
        item.quality = item.quality - 2 * qualityFactor;
        item.sellIn = item.sellIn - 1;
    }

    validateItems(): void {
        for (let i = 0; i < this.items.length; i++) {
            // quality never exceeds 50, except for Sulfuras
            if (!this.items[i].name.includes('Sulfuras') && this.items[i].quality > 50) {
                console.error(`Quality of item ${this.items[i].name} has exceeded 50!`);
                throw Error(`Quality of item ${this.items[i].name} has exceeded 50!`);
            }
            // quality is never less than 0
            if (this.items[i].quality < 0) {
                console.error(`Quality of item ${this.items[i].name} has become negative!`);
                throw Error(`Quality of item ${this.items[i].name} has become negative!`);
            }
        }
        console.log('Validation completed successfully!');
    }

    updateQuality(qualityFactor: number): Array<Item> {
        for (let i = 0; i < this.items.length; i++) {
            if (this.items[i].name.includes('Sulfuras')) {
                this.items[i].quality = 80;
                this.items[i].sellIn = this.items[i].sellIn - 1;
            } else if (this.items[i].name.includes('Aged Brie') || this.items[i].name.includes('Backstage passes')) {
                this.updateQualityForSpecialCases(this.items[i], qualityFactor);
            } else if (this.items[i].name === 'Conjured') {
                this.updateQualityForConjured(this.items[i], qualityFactor);
            } else {
                this.items[i].quality = this.items[i].quality - 1 * qualityFactor;
                this.items[i].sellIn = this.items[i].sellIn - 1;
            }
        }
        this.validateItems();
        return this.items;
    }
}