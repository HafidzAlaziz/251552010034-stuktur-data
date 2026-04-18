class TextEditor:
    def __init__(self):
        self.content = '' # teks aktif
        self.undo_stack = [] # riwayat state lama

    def write(self, teks):
        # Simpan state SEBELUM perubahan
        self.undo_stack.append(self.content)
        self.content += teks
        print(f'Tulis: {self.content}')

    def undo(self):
        if self.undo_stack: # ada riwayat?
            # Kembalikan ke state sebelumnya
            self.content = self.undo_stack.pop()
            print(f'UNDO → {self.content}')
        else:
            print('Tidak bisa undo lagi!')

            
editor = TextEditor()
editor.write('Mobil') # tulis konten
editor.write('Terbang') 
editor.undo() # UNDO 
editor.undo() # UNDO 