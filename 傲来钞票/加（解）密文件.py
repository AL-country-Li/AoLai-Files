#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AES-256-GCM 加密工具 - 修正版
适用于 cryptography 最新版本
"""

import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def encrypt_string(text, password):
    """
    加密字符串
    """
    # 生成随机盐值（32字节）和nonce（12字节）
    salt = os.urandom(32)
    nonce = os.urandom(12)
    
    # 从密码派生密钥（PBKDF2算法，10万次迭代）
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32字节 = 256位密钥
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password.encode('utf-8'))
    
    # 执行AES-GCM加密
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, text.encode('utf-8'), None)
    
    # 打包数据：salt + nonce + ciphertext
    combined = salt + nonce + ciphertext
    
    # 转为Base64便于存储/传输
    return base64.b64encode(combined).decode('ascii')

def decrypt_string(encrypted_b64, password):
    """
    解密字符串
    """
    # 解码Base64
    combined = base64.b64decode(encrypted_b64.encode('ascii'))
    
    # 提取各个部分
    salt = combined[:32]      # 前32字节是盐值
    nonce = combined[32:44]   # 接着12字节是nonce
    ciphertext = combined[44:] # 剩余是密文+认证标签
    
    # 用相同的参数重新派生密钥
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password.encode('utf-8'))
    
    # 解密并验证完整性
    aesgcm = AESGCM(key)
    try:
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
        return plaintext.decode('utf-8')
    except Exception as e:
        raise ValueError(f"解密失败！密码错误或数据已被篡改。错误：{e}")

# 命令行交互界面
if __name__ == "__main__":
    print("=" * 50)
    print("AES-256-GCM 加密工具")
    print("=" * 50)
    print("1. 加密文本")
    print("2. 解密文本")
    print("3. 退出")
    print("-" * 50)
    
    while True:
        choice = input("\n请选择操作 (1/2/3): ").strip()
        
        if choice == '1':
            # 加密模式
            text = input("请输入要加密的文本: ")
            password = input("请输入密码: ")
            
            try:
                encrypted = encrypt_string(text, password)
                print("\n✓ 加密成功！")
                print(f"密文: {encrypted}")
                print(f"\n【保存提示】请妥善保管密文和密码，两者缺一不可！")
            except Exception as e:
                print(f"✗ 加密失败: {e}")
                
        elif choice == '2':
            # 解密模式
            encrypted = input("请输入密文: ").strip()
            password = input("请输入密码: ")
            
            try:
                decrypted = decrypt_string(encrypted, password)
                print(f"\n✓ 解密成功！")
                print(f"原文: {decrypted}")
            except Exception as e:
                print(f"✗ 解密失败: {e}")
                
        elif choice == '3':
            print("再见！")
            break
        else:
            print("请输入 1、2 或 3")