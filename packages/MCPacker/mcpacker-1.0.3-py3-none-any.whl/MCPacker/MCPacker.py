# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import getopt
import sys
import os
import tempfile
import shutil
import subprocess
import json

from .__about__ import __version__
from semver import VersionInfo
from typing import List
from enum import IntEnum, unique


# -- Version components
@unique
class VersionComponent(IntEnum):
    Major = 1
    Minor = 2
    Patch = 3


# -- Classes
class MCPacker:
    """A tool to easily pack Minecraft addons."""

    def __init__(self, args):
        """Constructor based on command line arguments."""

        try:
            # -- Gather the arguments
            opts, arguments = getopt.getopt(args, 'hlvmM', ['help', 'license', 'version', 'minor', 'major'])

            self.component_to_increase: VersionComponent = VersionComponent.Patch

            for o, a in opts:
                if o in ('-h', '--help'):
                    MCPacker.printUsage()
                    sys.exit(0)
                elif o in ('-v', '--version'):
                    MCPacker.printVersion()
                    sys.exit(0)
                elif o in ('-l', '--license'):
                    MCPacker.printLicense()
                    sys.exit(0)
                elif o in ('-m', '--minor'):
                    if self.component_to_increase != VersionComponent.Patch:
                        raise RuntimeError('Can\'t specify both -m and -M on the command line.')

                    print("Increasing minor version...")
                    self.component_to_increase = VersionComponent.Minor
                elif o in ('-M', '--major'):
                    if self.component_to_increase != VersionComponent.Patch:
                        raise RuntimeError('Can\'t specify both -m and -M on the command line.')

                    print("Increasing major version...")
                    self.component_to_increase = VersionComponent.Major

            nb_of_arguments: int = len(arguments)
            if nb_of_arguments == 0:
                raise RuntimeError('Missing destination folder.')
            elif nb_of_arguments != 1:
                raise RuntimeError('Too many arguments.')

            self.destination_folder: str = arguments[0]
        except getopt.GetoptError:
            print('Unknown option or argument. Maybe start with `mcpack --help`?')
            sys.exit(0)

    def main(self) -> None:
        # cwd: str = os.getcwd()
        cwd = '/Users/didier/Documents/Code/Minecraft/The Dragon Mod'
        basename: str = os.path.basename(cwd).replace(' ', '')

        MCPacker.setupWorkFolder()

        manifest_file = os.path.join(cwd, 'manifest.json')
        if os.path.exists(manifest_file):
            MCPacker.increaseVersionNumberIn(manifest_file, self.component_to_increase)

            uuid, version = MCPacker.getPackInfoFrom(manifest_file)
            if uuid is None:
                raise RuntimeError('Can\'t get information from a pack we created earlier.')

            MCPacker.pack(cwd, os.path.join(self.destination_folder, basename + '-' + str(version) + '.mcpack'))
            return

        source_packs: List[str] = MCPacker.listManifestFilesFromPacksIn(cwd)
        for manifest_file in source_packs:
            MCPacker.increaseVersionNumberIn(manifest_file, self.component_to_increase)

        MCPacker.syncVersionNumbers(cwd)

        addon_version: VersionInfo = None

        for manifest_file in source_packs:
            uuid, version = MCPacker.getPackInfoFrom(manifest_file)
            if uuid is None:
                raise RuntimeError('Can\'t get information from a pack we created earlier.')

            if addon_version is None or version > addon_version:
                addon_version = version

            pack_folder: str = os.path.dirname(manifest_file)
            MCPacker.pack(pack_folder, os.path.join(MCPacker.workFolder(), os.path.basename(pack_folder) + '-' + str(version) + '.mcpack'))

        MCPacker.pack(MCPacker.workFolder(), os.path.join(self.destination_folder, basename + '-' + str(addon_version) + '.mcaddon'))

    def shutdown(self) -> None:
        print("Done.")

    @classmethod
    def syncVersionNumbers(cls, folder: str):
        print("Syncing versions numbers...")

        versions = {}
        manifest_files: List[str] = MCPacker.listManifestFilesFromPacksIn(folder)
        for manifest_file in manifest_files:
            uuid, version = MCPacker.getPackInfoFrom(manifest_file)
            if uuid is not None:
                versions[uuid] = version

        for manifest_file in manifest_files:
            file = open(manifest_file, 'r')
            json_data = json.load(file)
            file.close()

            dependencies = json_data.get('dependencies')
            if dependencies is None:
                continue

            for dependency in dependencies:
                uuid = dependency.get('uuid')
                if uuid is None:
                    continue

                new_version = versions.get(uuid)
                if new_version is None:
                    continue

                json_version = dependency.get('version')
                if json_version is not None and len(json_version) == 3:
                    MCPacker.setVersionInJsonElement(new_version, json_version)

                    file = open(manifest_file, 'w')
                    json.dump(json_data, file, indent=2)
                    file.close()

    @classmethod
    def getPackInfoFrom(cls, manifest_file: str):
        file = open(manifest_file, 'r')
        json_data = json.load(file)
        file.close()

        header = json_data.get('header')
        if header is not None:
            version = header.get('version')
            if version is not None and len(version) == 3:
                uuid = header.get('uuid')
                if uuid is not None:
                    return uuid, VersionInfo.parse(f'{version[0]}.{version[1]}.{version[2]}')

        return None, None

    @classmethod
    def increaseVersionNumberIn(cls, manifest_file: str, which_component: VersionComponent = VersionComponent.Patch):
        file = open(manifest_file, 'r')
        json_data = json.load(file)
        file.close()

        modified_something = False

        header = json_data.get('header')
        if header is not None:
            modified_something = MCPacker.increaseVersionIn(header, which_component)

        modules = json_data.get('modules')
        if modules is not None:
            for module in modules:
                modified_something = MCPacker.increaseVersionIn(module, which_component)

        if modified_something:
            file = open(manifest_file, 'w')
            json.dump(json_data, file, indent=2)
            file.close()

    @classmethod
    def setVersionInJsonElement(cls, version: VersionInfo, json_element) -> bool:
        json_element[0] = version.major
        json_element[1] = version.minor
        json_element[2] = version.patch

    @classmethod
    def increaseVersionIn(cls, json_element: List, which_component: VersionComponent = VersionComponent.Patch) -> bool:
        json_version = json_element.get('version')
        if json_version is None and len(json_version) != 3:
            return False

        old_semver_version = VersionInfo.parse(f'{json_version[0]}.{json_version[1]}.{json_version[2]}')

        if which_component == VersionComponent.Major:
            new_semver_version = old_semver_version.bump_major()
        elif which_component == VersionComponent.Minor:
            new_semver_version = old_semver_version.bump_minor()
        else:
            new_semver_version = old_semver_version.bump_patch()

        MCPacker.setVersionInJsonElement(new_semver_version, json_version)

        json_desc = json_element.get('description')
        if json_desc is not None:
            json_element['description'] = json_desc.replace('v' + str(old_semver_version), 'v' + str(new_semver_version))

        return True

    @classmethod
    def pack(cls, source_folder: str, destination_file: str):
        basename: str = os.path.basename(destination_file)
        print(f'Packing {basename}...')

        arguments: List[str] = ['zip', '-r', destination_file]
        for sub_entry in os.listdir(source_folder):
            arguments.append(sub_entry)

        arguments += ['-x', '*.DS_Store']

        MCPacker.shellCommand(arguments, source_folder)

    @classmethod
    def listManifestFilesFromPacksIn(cls, folder: str):
        source_packs: List[str] = []

        for entry in os.listdir(folder):
            entry_full_path: str = os.path.join(folder, entry)
            if not os.path.isdir(entry_full_path):
                continue

            manifest_file: str = os.path.join(entry_full_path, 'manifest.json')
            if os.path.exists(manifest_file):
                source_packs.append(manifest_file)

        return source_packs

    @classmethod
    def setupWorkFolder(cls):
        work_folder = MCPacker.workFolder()
        if os.path.exists(work_folder):
            shutil.rmtree(work_folder, ignore_errors=True)

        os.makedirs(work_folder)

    @classmethod
    def workFolder(cls):
        return os.path.join(tempfile.gettempdir(), 'net.malenfant.mcpacker')

    @classmethod
    def shellCommand(cls, command_and_args: List[str], from_dir: str):
        try:
            process = subprocess.Popen(command_and_args, cwd=from_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                print(command_and_args)
                print(stdout)
                print(stderr)

                raise RuntimeError('Error running shell command.')
        except RuntimeError:
            raise
        except SyntaxError:
            raise
        except Exception as e:
            raise RuntimeError('Error running shell command: ' + str(e))

    @classmethod
    def printUsage(cls) -> None:
        MCPacker.printVersion()
        print('')
        print('usage: mcpack <options> destination_folder')
        print('')
        print('The following options are supported:')
        print('')
        print('   --help/-h          - Show a help message.')
        print('   --version/-v       - Display the app\'s version.')
        print('   --license/-l       - Display the app\'s license.')
        print('   --minor/-m         - Bump the minor version instead of the patch version.')
        print('   --major/-M         - Bump the major version instead of the patch version.')
        print('')

    @classmethod
    def printVersion(cls) -> None:
        print('🕹  MCPacker v' + __version__ + ' 🕹')

    @classmethod
    def printLicense(cls):
        MCPacker.printVersion()
        print('')
        print('MIT License')
        print('')
        print('Copyright (c) 2022-present Didier Malenfant <coding@malenfant.net>')
        print('')
        print('Permission is hereby granted, free of charge, to any person obtaining a copy')
        print('of this software and associated documentation files (the "Software"), to deal')
        print('in the Software without restriction, including without limitation the rights')
        print('to use, copy, modify, merge, publish, distribute, sublicense, and/or sell')
        print('copies of the Software, and to permit persons to whom the Software is')
        print('furnished to do so, subject to the following conditions:')
        print('')
        print('The above copyright notice and this permission notice shall be included in all')
        print('copies or substantial portions of the Software.')
        print('')
        print('THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR')
        print('IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,')
        print('FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE')
        print('AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER')
        print('LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,')
        print('OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE')
        print('SOFTWARE.')
        print('')
        print('Official repo can be found at https://codeberg.org/DidierMalenfant/MCPack')
        print('')
